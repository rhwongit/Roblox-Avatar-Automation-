# 🖼️ Python Avatar Automation

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) 

Automate Roblox avatar outfit changes with Python! This script cycles through your favorite outfits automatically every hour using your Roblox cookie.

---

## ✨ Features

- 🟢 Log in securely using your Roblox `.ROBLOSECURITY` cookie  
- 🟢 Automatically cycle through multiple outfits  
- 🟢 Works continuously every hour  
- 🟢 Lightweight and easy to set up  

---

## 🚀 Tech Stack

- **Python 3.x**  
- **Libraries:** `requests`  
- **Platform:** Cross-platform (Windows, Linux, macOS)  

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-avatar-automation.git
cd python-avatar-automation

# Install dependencies
pip install requests

🔑 Setup Your Roblox Cookie

    Create a file named cookie.txt in the project root.

    Paste your Roblox .ROBLOSECURITY cookie inside the file.

    Save the file.

    ⚠️ Keep this cookie private! Sharing it can compromise your account.

🛠️ Configure Outfits

    Open avatar_automation.py (or your script file).

    Replace the IDs in the OUTFITS list with your desired Roblox outfit IDs:

OUTFITS = [123456789, 987654321]  # Replace with your Outfit IDs

🖥️ Usage

Run the script:

python avatar_automation.py

    The script will log in using your cookie

    It will automatically cycle through the outfits you configured

    Waits 1 hour between outfit changes

Example console output:

✅ Logged in as: YourUsername (UserId: 123456)
✅ Changed outfit to 123456789
⏳ Waiting 1 hour...
✅ Changed outfit to 987654321
⏳ Waiting 1 hour...

⏱️ Automation Notes

    The script uses an infinite loop to cycle outfits every hour

    You can adjust the interval by changing time.sleep(3600) (3600 seconds = 1 hour)

🎨 Customization

    Add as many outfit IDs as you want

    Adjust the timing interval to your preference

    Combine with task schedulers (Windows Task Scheduler, cron) for advanced automation

🤝 Contributing

Contributions are welcome!

    Fork the repository

    Create a feature branch: git checkout -b feature-name

    Make your changes

    Push and submit a pull request
