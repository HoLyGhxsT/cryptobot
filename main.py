from dotenv import load_dotenv
import discord, requests, os, logging
from discord.ext import tasks
from datetime import datetime

load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]
GUILD = os.environ["GUILD"]
CHANNEL = os.environ["CHANNEL"]


def getCryptoPrices():
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=jumptoken&vs_currencies=inr%2Cusd"
    r = requests.get(url=URL)
    data = r.json()
    inr = data["jumptoken"]["inr"]
    usd = data["jumptoken"]["usd"]
    # print(data)
    # return data, inr, usd
    return [data, inr, usd]


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

# client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    channel = discord.utils.get(client.get_all_channels(), name="test")
    # await client.get_channel(channel.id).send('Bot is now Online!')
    # return channel
    print("--------------------------------------------------")
    # auto_send.start()
    # print("Auto send data initialized. Sends data every hours starting now...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Message from {message.author}: {message.content}")

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    elif message.content.startswith("jmptplain"):
        await message.channel.send(getCryptoPrices())
    elif message.content.startswith("jmpt"):
        # data, inr, usd = getCryptoPrices()
        dat = getCryptoPrices()
        embed = discord.Embed(
            title="JumpToken Price Now",
            url="https://www.coingecko.com/en/coins/jumptoken",
            # description=f"1 JMPT in INR {inr}₹\n 1 JMPT in USD {usd}$",
            description=f"1 JMPT in INR {dat[1]}₹\n 1 JMPT in USD {dat[2]}$",
            timestamp=datetime.now()
        )
        embed.set_thumbnail(
            url="https://s2.coinmarketcap.com/static/img/coins/200x200/17334.png"
        )
        await message.channel.send(embed=embed)
    elif message.content.startswith("ping"):
        # await message.channel.send('Pong! {0}'.format(round(client.latency, 1)))
        embed = discord.Embed(
            title="Pong 🏓",
            description=f"Latency : {round(client.latency * 1000)}ms",
            color=0x10B900,
        )
        await message.channel.send(embed=embed)
    elif message.content.startswith("help"):
        embed = discord.Embed(title="Help 😣", description=f" Ping \n jmpt \n jmptplain")
        await message.channel.send(embed=embed)


@tasks.loop(hours=1)
async def auto_send():
    channel = client.get_channel(int(CHANNEL))
    dat = getCryptoPrices()
    embedauto = discord.Embed(
        title="JumpToken Price Now",
        url="https://www.coingecko.com/en/coins/jumptoken",
        description=f"1 JMPT in INR {dat[1]}₹\n 1 JMPT in USD {dat[2]}$",
        timestamp=datetime.now()
    )
    embedauto.set_thumbnail(
        url="https://s2.coinmarketcap.com/static/img/coins/200x200/17334.png"
    )
    await channel.send(embed=embedauto)
    write_to_log()


def write_to_log():
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    # print(current_date_time)

    with open("run.log", mode="a") as file:
        # file.write("Recorded at %s.\n" % (datetime.datetime.now()))
        file.write(f"Runned at {current_date_time} {getCryptoPrices()} \n")
        file.close()


# @tasks.loop(seconds=5)
# async def autosend():
#    # channel = discord.utils.get(client.get_all_channels(), name='test')
#    channel = client.get_channel()
#    embed = discord.Embed(title="JumpToken Now", url="https://www.coingecko.com/en/coins/jumptoken",
#                          description=f'{getCryptoPrices()}')
#    await channel.send(embed=embed)


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
# client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
client.run(TOKEN)
