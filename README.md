# SnusBase bot

> **A simple bot for SnusBase search (big database) with `experimental API` URL and ApiKey. Enjoy!**

```
SNUSBASE PYTHON  BOT
  └── 🌐 Help command
       ├── ☝️ .snusbase <username>
       ├── 🛠️ .snusbase <email>
       ├── 🚀 .snusbase <ip>
       ├── ❓.snusbase <password> 
       ├── 🎉 .snusbase <hash>
       └── 📫 .snusbase <name>
```

> **Auto Installing `libraries`**

```python
import os

try:
    import discord, requests, json, asyncio
    from colorama import Fore
    from discord.ext import commands

except:
    os.system('pip install discord.py requests asyncio colorama')
```

<hr>

- **1. Clone or download the `repository`**

> **For `Linux`:**

```shell
git clone https://github.com/gqkfh/snusbase-bot 
```

> **For `Windows`:**

```
- Download the .zip file and decompress it
```

-  **2. `Replace your data` in the config.json file**

```json
{
    "token": "YOUR_BOT_TOKEN",
    "activity": "YOUR_BOT_ACTIVITY",
    "prefix": "YOUR_BOT_PREFIX",
    "embedColor": "YOUR_MESSAGE_COLOR",
    "author": "YOUR_USERNAME"
}
```

- **3. Execute the `main.py`**

```shell
python main.py
```
