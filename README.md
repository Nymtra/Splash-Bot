
# 🌊 Splash-Bot  

![Splash Bot Title](img/splasher.png)  

A Discord bot that randomly selects splash screens (`.bmp`) from [Mayhem-Splashes](https://github.com/Nymtra/Mayhem-Splashes), converts them to `.png`, and sends them in style.  

---

## ✨ Features  
- 🎲 Random splash screen selection from GitHub.  
- 🖼 Converts `.bmp` → `.png` automatically.  
- 📎 Sends an embed with:  
  - Inline preview  
  - **Download BMP** button  
  - **Visit Website** button  
- ⚡ Easy-to-use slash command: `/splash`.  

---

## 📦 Installation  

### 1. Clone the repo  
```bash
git clone https://github.com/yourusername/Splash-Bot.git
cd Splash-Bot
````

### 2. Install requirements

Make sure Python 3.10+ is installed, then:

```bash
pip install -r requirements.txt
```

Dependencies:

* `discord.py` (2.0+)
* `aiohttp`
* `Pillow`

### 3. Configure token

In your bot file, replace:

```python
TOKEN = "your Token here"
```

with your actual bot token.

---

## 🚀 Usage

Run the bot:

```bash
python bot.py
```

Then in Discord, type:

```
/splash
```

👉 The bot will fetch a random splash, convert it, and reply with an embed + buttons.

---

## 🖼 Screenshots

### Bot Response Example

![Bot Response](img/splasher1.png)

### Hosted Website Preview

![Website Preview](img/splasher2.png)

---

## 🔗 Links

* 🌐 [Main Website](https://nymtra.github.io/splashes)
* 📂 [Splash Repository](https://github.com/Nymtra/Mayhem-Splashes)

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).

```


