# Discord Custom Rich Presence

A lightweight, fully customizable Discord Rich Presence (RPC) tool written in Python.  
Easily display custom status text, dynamic timestamps, custom images, and interactive buttons on your Discord profile.

---

## Features

- **Custom Text**: Set your own status details and state.
- **Images & Assets**: Support for large and small rich presence assets.
- **Interactive Buttons**: Add up to 2 clickable link buttons (Discord, YouTube, Twitch, etc.).
- **Elapsed Time**: Automatically tracks and displays elapsed play/work time.
- **No Token Required**: Safe and secure using standard Discord IPC connection.

---

## Setup & Usage

### 1. Prerequisites
- Python 3.8 or higher installed on your system.
- Discord desktop client running.

### 2. Installation
Clone this repository or download the ZIP file:
```bash
git clone [https://github.com/All-Is-Lost/discord-custom-rpc.git](https://github.com/All-Is-Lost/discord-custom-rpc.git)
cd discord-custom-rpc
pip install -r requirements.txt
```

### 3. Configuration
1. Open the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a **New Application** and copy your **Application ID**.
3. Under **Rich Presence -> Art Assets**, upload your images and note their asset keys.
4. Edit `config.json` with your details:

```json
{
  "client_id": "YOUR_APPLICATION_ID_HERE",
  "details": "Playing Online",
  "state": "In Match",
  "large_image": "logo",
  "large_text": "Game Title",
  "small_image": "icon",
  "small_text": "Online",
  "buttons": [
    {
      "label": "Visit Profile",
      "url": "[https://github.com/All-Is-Lost](https://github.com/All-Is-Lost)"
    },
    {
      "label": "Join Discord",
      "url": "[https://discord.gg/](https://discord.gg/)"
    }
  ]
}
```

### 4. Run the Script
```bash
python main.py
```

---

## Support & Donations

If you find this project useful, consider buying me a coffee! Any support is greatly appreciated.

[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/YOUR_KOFI_USERNAME)

---

## License

MIT License
