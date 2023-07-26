from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from dotenv import load_dotenv
from discord import Member, VoiceState, Client
import os
import discord
import random

from music import Music, EmptyQueue
from utils import search_song
from command_info import send_bot_help
from voice_channel_actions import leave_after_being_left_alone
from member_greetings import send_random_message

activity = discord.Activity(
    type=discord.ActivityType.listening,
    name="guaracha"
)
intents = discord.Intents.all()
client: Client = commands.Bot(command_prefix="Luna ",
                              intents=intents, activity=activity)
music = Music()
load_dotenv()
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")

PAUSE_RESPONSES = [
    "Oigan a esta ridícula, si la canción ya está pausada",
    "Reina, la canción está en pausa",
    "No así sí perdiste mor, la canción está en pausa",
    "Deje dormir ome, eh",
    "Ya está pausada, tan boba"
]

BYE_RESPONSES = [
    "No ps tan creída",
    "Qué horror qué pena, ps, en el 2020 y pasando este tipo de cosas?",
    "Tan creída esta zpa perra"
]


@client.event
async def on_voice_state_update(member: Member, before: VoiceState, after: VoiceState):
    if after.channel and not member.bot and not before.channel:
        print("Someone joined")
        await send_random_message(member, client)
    if (before.channel and len(before.channel.members) == 1):
        player = music.get_player(guild_id=before.channel.guild.id)
        if (player):
            player.delete()
        await leave_after_being_left_alone(member, before, client)


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        print(channel)
        if str(channel) == "general":
            await channel.send("Kemás ps gordoss, llegó la más embolatada 💋")
            await channel.send("https://tenor.com/view/tulleras-gif-21992652")


@client.event
async def on_message(message):
    ctx = await client.get_context(message)

    if message.author == client.user:
        return

    if message.content == "purebita":
        await message.channel.send("holis")

    if message.content == "Hola Luna":
        await message.channel.send("Qué más pues 💋")

    await client.process_commands(message)


@client.command(name="join")
async def join(ctx):
    await ctx.author.voice.channel.connect()


@client.command(name="play")
async def play(ctx):
    song_request = ctx.message.content[10:]
    if ctx.author.voice is None:
        await ctx.send("Mor, entre a un canal de voz pss")
        return
    channel = ctx.author.voice.channel

    if "youtube.com" in song_request or "youtu.be" in song_request:
        video_url = song_request
    else:
        video_url = await search_song(client, 1, song_request, True)

    if ctx.voice_client is None:
        await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)

    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(video_url, search=True)
        song = await player.play()
        await ctx.send(f"Poniendo: {song.name}")
    else:
        song = await player.queue(video_url, search=True)
        await ctx.send(f"Mor, ahorita pongo: {song.name}")


@client.command(name="pause")
async def pause(ctx):
    if ctx.voice_client is None:
        await ctx.send("Mor, ni estoy tocando, tan boba")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await ctx.send(random.choice(PAUSE_RESPONSES))
        return
    ctx.guild.voice_client.pause()
    emoji = '\N{RAISED HAND}'
    await ctx.message.add_reaction(emoji)


@client.command(name="resume")
async def resume(ctx):
    if ctx.voice_client is None:
        await ctx.send("Mor, ni estoy tocando, tan boba")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        ctx.guild.voice_client.resume()
        emoji = '\N{DANCER}'
        await ctx.message.add_reaction(emoji)
    else:
        await ctx.send("Mor, la canción no está pausada")


@client.command(name="chao")
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send("Ni estoy conectada y ya me está echando, gos.")
    else:
        player = music.get_player(guild_id=ctx.guild.id)
        if player:
            player.delete()
        await ctx.send(random.choice(BYE_RESPONSES))
        await ctx.send(f"Vea, esta care rara me echó {ctx.message.author.mention}")
        await ctx.voice_client.disconnect()


@client.command(name="skip")
async def skip(ctx):
    if ctx.voice_client is None:
        await ctx.send("Mor, ni estoy tocando, tan boba")
        return
    player = music.get_player(guild_id=ctx.guild.id)
    try:
        data = await player.skip()
    except EmptyQueue:
        await ctx.send("Tan amurada esta zpa, no hay cola")
        return
    await ctx.send(f"Quité: {data[0].name}")
    await ctx.send(f"Y puse: {data[1].name}")


@client.command(name="ayuda")
async def send_help(ctx):
    await send_bot_help(ctx.channel)
client.run(CLIENT_TOKEN)
