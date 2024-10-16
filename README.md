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

> **Auto Installing libraries**

```python
import os

try:
    import discord, requests, json, asyncio
    from colorama import Fore
    from discord.ext import commands

except:
    os.system('pip install discord.py requests asyncio colorama')
```
