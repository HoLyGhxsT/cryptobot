import os
import logging
import logging.handlers
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
# TOKEN = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# logging.getLogger('discord.http').setLevel(logging.INFO)

# handler = logging.handlers.RotatingFileHandler(
#     filename='discord.log',
#     encoding='utf-8',
#     maxBytes=32 * 1024 * 1024,  # 32 MiB
#     backupCount=5,  # Rotate through 5 files
# )
# dt_fmt = '%Y-%m-%d %H:%M:%S'
# formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
