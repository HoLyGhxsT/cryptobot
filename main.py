import discord
import requests, os
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['GUILD']

def getCryptoPrices():
    URL = 'https://api.coingecko.com/api/v3/simple/price?ids=jumptoken&vs_currencies=inr%2Cusd'
    r = requests.get(url=URL)
    data = r.json()
    # print(data)
    return data


client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'Logged In')
    channel = discord.utils.get(client.get_all_channels(), name='test')
    #await client.get_channel(channel.id).send('Bot is now Online!')
    #return channel
    
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hey':
        print('hey')
        await message.channel.send('hola')
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    
    #    if message.content.startswith('hi'):
#        await message.channel.send('hey')

# if message.content.startswith('tell'):
    #     embed = discord.Embed(title="JumpToken Now", url="https://www.coingecko.com/en/coins/jumptoken",
    #                           description=f'{getCryptoPrices()}')
    #     await message.channel.send(embed=embed)


#@tasks.loop(seconds=5)
#async def autosend():
#    # channel = discord.utils.get(client.get_all_channels(), name='test')
#    channel = client.get_channel(849994742150594571)
#    embed = discord.Embed(title="JumpToken Now", url="https://www.coingecko.com/en/coins/jumptoken",
#                          description=f'{getCryptoPrices()}')
#    await channel.send(embed=embed)

# @my_background_task.before_loop


#async def my_background_task_before_loop():
 #   await client.wait_until_ready()

#autosend.start()
client.run(TOKEN)
