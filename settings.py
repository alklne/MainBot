import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_TOKEN")
OWNER_ID = 877978367964610570