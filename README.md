# 🎮 Roblox Avatar Automation

Automate your Roblox avatar outfit changes effortlessly with Python. Keep your avatar looking fresh by cycling through your favorite outfits automatically!

---

## ✨ Features

* 🔒 **Secure login** using your Roblox `.ROBLOSECURITY` cookie
* 👕 **Automatic outfit rotation**
* ⚡ **Lightweight** and runs continuously in the background
* 💻 **Cross-platform**: Windows, Linux, macOS

---

## 🛠️ Tech Stack

* 🐍 Python 3.x
* 📦 `requests` library
* 🌐 Cross-platform

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/roblox-avatar-automation.git
cd roblox-avatar-automation

# Install dependencies
pip install requests
```

---

## 🔑 Setup

### Step 1 — Get Your Roblox Cookie

1. Open Roblox and log in.
2. Press **F12** → **Network** tab.
3. Refresh the page and click any request to `roblox.com`.
4. Under **Request Headers**, find:

```
Cookie: .ROBLOSECURITY=YOUR_COOKIE_HERE
```

5. Copy everything after `=`.
6. Create a file called `cookie.txt` in the project root and paste your cookie.

⚠️ **Keep this cookie private** — leaking it can compromise your account.

### Step 2 — Configure Outfits

Edit `avatar_automation.py` and update the outfit IDs with your preferred ones. Example with clean random numbers and friendly names:

```python
OUTFITS = {
    1012345678901234: "Chill Vibes",
    2023456789012345: "Street Style",
    3034567890123456: "Classic Cool",
    4045678901234567: "Urban Explorer",
    5056789012345678: "Night Rider",
    6067890123456789: "Summer Breeze"
}
```

---

## ▶️ Usage

Run the script:

```bash
python avatar_automation.py
```

It will:

* ✅ Log in using your cookie
* 👕 Switch outfits randomly
* ⏱️ Wait 1 hour before changing again

**Sample output:**

```
✅ Logged in as: TERMINATORR60 (UserId: 4755568233)
✨ Wore outfit: Chill Vibes (ID: 1012345678901234)
⏳ Waiting 1 hour...
✨ Wore outfit: Street Style (ID: 2023456789012345)
⏳ Waiting 1 hour...
```

---

## ⏱️ Notes

* Default interval: **1 hour** (`time.sleep(3600)`)
* Adjust interval for faster or slower outfit changes
* For automation:

  * 🗓️ Windows Task Scheduler
  * ⏰ Cron jobs on Linux/macOS

---

## 🎨 Customization

* Add or remove outfit IDs
* Adjust interval timing
* Extend with features like:

  * 🎲 Randomizer
  * 📋 Alerts or logs
  * 📸 Avatar screenshots

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit and push your changes
4. Open a pull request

---

✨ Stay stylish automatically! ✨
