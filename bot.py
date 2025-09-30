import random, aiohttp
from io import BytesIO
from PIL import Image
import discord
from discord.ext import commands


# sum vars
TOKEN = "your Token here"
GITHUB_API = "https://api.github.com/repos/Nymtra/Mayhem-Splashes/contents/"
MAIN_WEBSITE = "https://nymtra.github.io/splashes"

# intents and prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
# msg on ready
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"logged in lol{bot.user}")
# creating the buttons
class LinkButtons(discord.ui.View):
    def __init__(self, bmp_url):
        super().__init__()
        self.add_item(discord.ui.Button(label="Download Splash", url=bmp_url, style=discord.ButtonStyle.link)) # blue
        self.add_item(discord.ui.Button(label="Main Page", url=MAIN_WEBSITE, style=discord.ButtonStyle.secondary)) # gray
# /splash command
@bot.tree.command(name="splash", description="random .bmp splas")
async def splash(interaction: discord.Interaction):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(GITHUB_API) as resp:
            data = await resp.json()
            bmps = [f for f in data if f["name"].lower().endswith(".bmp")]
            if not bmps:
                await interaction.followup.send("No .bmp found")
                return
            pick = random.choice(bmps)
            url = pick["download_url"]

            async with session.get(url) as img_resp:
                bmp_bytes = await img_resp.read()

            # conv bmp to png
            bmp_image = Image.open(BytesIO(bmp_bytes))
            png_buffer = BytesIO()
            bmp_image.save(png_buffer, format="PNG")
            png_buffer.seek(0)
            # set file
            file = discord.File(fp=png_buffer, filename=pick["name"].replace(".bmp", ".png"))
            # create embed
            embed = discord.Embed(
                title=pick["name"],
                color=discord.Color.blue()
            )
            # add image to embed
            embed.set_image(url=f"attachment://{pick['name'].replace('.bmp', '.png')}")
            # add the buttons
            view = LinkButtons(bmp_url=url)
            await interaction.followup.send(embed=embed, file=file, view=view)

bot.run(TOKEN)
