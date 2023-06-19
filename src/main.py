from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from dotenv import load_dotenv
import os
import discord

from music import Music

activity = discord.Activity(
    type=discord.ActivityType.watching,
    name="Vídeos de Luna Gil"
)
intents = discord.Intents.all()
client = commands.Bot(command_prefix="Parce ",
                      intents=intents, activity=activity)
music = Music()
load_dotenv()
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")


@client.event
async def on_message(message):
    ctx = await client.get_context(message)

    if message.author == client.user:
        return

    if message.content == "Hola parcera":
        await message.channel.send("Qué más pues reina hermosa 💋")

    await client.process_commands(message)


@client.command(name="play")
async def play(ctx, name):
    await ctx.send(name)

client.run(CLIENT_TOKEN)
