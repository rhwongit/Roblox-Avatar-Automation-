# 🎭 Roblox Avatar Automation

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)  
[![Requests](https://img.shields.io/badge/Library-requests-green)](https://pypi.org/project/requests/)  
[![Platform](https://img.shields.io/badge/Platform-Roblox-red?logo=roblox)](https://www.roblox.com)  

Automate your **Roblox avatar outfit changes** with Python. Supports both **R6 and R15 avatars** and allows random or scheduled outfit switching.  

---

## ✨ Features

- 🔐 Secure login using `.ROBLOSECURITY` cookie  
- 👕 Automatically wear saved Roblox outfits  
- 🎯 Supports **R6, R15, or both avatars**  
- ⚡ Lightweight, runs in the background  
- 📝 Logs outfits and assets to JSON/TXT for inspection  
- ⏱️ Automatic random outfit cycling (configurable interval)  
- 🖥️ Cross-platform: Windows, Linux, macOS  

---

## 🛠️ Tech Stack

- 🐍 Python 3.13.7  
- 📦 `requests` library  
- 🌍 Roblox platform API  

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/yourusername/roblox-avatar-automation.git
cd roblox-avatar-automation

# Install dependencies
pip install requests

🔑 Setup
1️⃣ Get your Roblox cookie

    Log in to Roblox on your browser.

    Press F12 → Network → refresh page → click any request to roblox.com.

    Find .ROBLOSECURITY cookie and copy the value.

    Create cookie.txt in project root and paste your cookie.

⚠️ Keep your cookie private. Sharing it gives access to your account.
2️⃣ Choose Avatar Type

    When running the logger or wearer script, you will be prompted to choose:

        R6 → Only fetch/wear R6 outfits

        R15 → Only fetch/wear R15 outfits

        Both → Fetch/wear both

📸 Sample Output

Logger Example:

✅ Logged in as: RobloxUser (UserId: 4755568233)
✨ Found 42 outfits total. Filtering R6 editable outfits...
✅ Found 8 saved R6 outfits.
✅ Saved outfits with asset IDs to outfits_r6.json
✅ Also saved a readable version to outfits_r6.txt

Wearer Example:

✅ Wore outfit: Supreme (R6)
⏳ Waiting 30 minutes before next outfit...
✅ Wore outfit: Tokyo 10 (R15)
⏳ Waiting 30 minutes before next outfit...

⚙️ Usage
1️⃣ Run the assetID logger to fetch saved outfits

python AssetID_combined.py

    Generates:

        outfits_r6.json / .txt

        outfits_r15.json / .txt

    Only editable outfits are saved

    Only outfits matching the chosen avatar type are logged

2️⃣ Run the wearer script to cycle outfits

python Wearer_combined.py

    Prompts for avatar type to wear

    Randomly cycles through saved outfits every 10 minutes (configurable)

    Applies body colors and avatar type properly to avoid default Roblox look

🎨 Customization

    Change interval by modifying time.sleep() in wearer_combined.py

    Add/remove outfits manually in the JSON files

    Extend the logger or wearer with additional features like alerts or logging failed outfits

🤝 Contributing

Contributions are welcome!

    Fork the repository

    Create a feature branch (git checkout -b feature-name)

    Commit and push

    Open a pull request

⚡ Notes

    R6 outfits will always match your R6 avatar, R15 outfits for R15

    Only editable outfits can be worn automatically

    Failed outfits can be logged manually by inspecting TXT/JSON files

📂 File Structure

roblox-avatar-automation/
├─ cookie.txt           # Your Roblox cookie
├─ AssetID_combined.py   # Fetches and logs outfits
├─ Wearer_combined.py   # Wears outfits in cycles
├─ outfits_r6.json      # Saved R6 outfits
├─ outfits_r6.txt       # Human-readable R6 outfits
├─ outfits_r15.json     # Saved R15 outfits
├─ outfits_r15.txt      # Human-readable R15 outfits

✨ Stay stylish, automatically! ✨
