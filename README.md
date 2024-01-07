# AntiLinkLeak
## __does NOT leak links__
Simply checks against Deblok's public link leaker spreadsheet every member join/leave. Updates local cache periodically.

- To setup (Linux, specifically Debian-based syntax):
```bash
pip install -r requirements.txt
mkdir env 
touch token.txt
echo YOUR_BOT_TOKEN > env/token.txt # token.txt fallback
export $BOT_TOKEN=YOUR_BOT_TOKEN # environment variable
```

- To setup (Windows)
```batch
pip install -r requirements.txt
mkdir env
rem token.txt fallback
echo YOUR_BOT_TOKEN > env/token.txt
rem environment variable
set BOT_TOKEN=YOUR_BOT_TOKEN
```

Invite the official bot [**here**](https://discord.com/api/oauth2/authorize?client_id=1189290892486516737&permissions=274877908996&scope=bot%20applications.commands)
