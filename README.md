# 🎭 Roblox Avatar Automation

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Library-requests-green.svg)](https://pypi.org/project/requests/)
[![Roblox](https://img.shields.io/badge/Platform-Roblox-red.svg?logo=roblox)](https://www.roblox.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

Automatically cycle through your Roblox outfits using Python.  
This script changes your avatar every hour so you always look fresh without lifting a finger.

---

## ✨ Features
- 🔐 Secure login with your Roblox **.ROBLOSECURITY** cookie  
- 👕 Rotate through multiple outfits automatically  
- ⚡ Lightweight, runs continuously in the background  
- 💻 Works on Windows, Linux, and macOS  

---

## 🛠️ Tech Stack
- 🐍 Python 3.x  
- 📦 `requests` library  
- 🌍 Cross-platform  

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/roblox-avatar-automation.git
cd roblox-avatar-automation

# Install dependencies
pip install requests

🔑 Setup
Step 1 — Get Your Roblox Cookie

    Open Roblox

and log in.

Press F12 (Developer Tools) → Network tab.

Refresh the page.

Click on any request to roblox.com.

Under Request Headers, find:

    Cookie: .ROBLOSECURITY=YOUR_COOKIE_HERE

    Copy everything after =.

    Create a file called cookie.txt in the project root and paste your cookie.

⚠️ Keep this cookie private — leaking it means losing your account.

📸 Example:
Step 2 — Configure Outfits

Edit avatar_automation.py and update the outfit IDs:

OUTFITS = [
    1234567890123456,  # Streetwear
    9876543210987654,  # Samurai
    1928374655647382,  # Classic Suit
    5647382910123456   # Casual Hoodie
]

📸 Example:
▶️ Usage

Run the script:

python avatar_automation.py

It will:

    ✅ Log in with your cookie

    👕 Switch outfits one by one

    ⏱️ Wait 1 hour before changing again

Sample output:

Logged in as: YourUsername (UserId: 123456)
Changed outfit to 1234567890123456 (Streetwear)
⏳ Waiting 1 hour...
Changed outfit to 9876543210987654 (Samurai)
⏳ Waiting 1 hour...

⏱️ Notes

    Default interval = 1 hour (time.sleep(3600))

    Adjust freely for shorter/longer waits

    For automation:

        ⏺️ Use Windows Task Scheduler

        ⏺️ Or cron jobs on Linux/macOS

🎨 Customization

    Add/remove outfit IDs

    Change interval timing

    Extend with more features (randomizer, alerts, etc.)

🤝 Contributing

Contributions are welcome!

    Fork this repo

    Create a feature branch (git checkout -b feature-name)

    Commit and push

    Open a pull request

✨ Stay stylish, automatically! ✨
