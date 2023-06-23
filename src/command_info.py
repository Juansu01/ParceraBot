import discord


async def send_bot_help(channel):
    """
    Sends and embedded message with information about the
    Bot's commmands.
    """

    embed = discord.Embed(title="Comandos de Luna",
                          description="Pa que la utilicen bien pss, prefijo \"Luna\"")
    embed.add_field(name="play <Nombre o URL>",
                    value="Pa colocar una canción, pa qué más xd, "
                    "si ya hay una canción sonando, la nueva"
                    " se agrega a la cola")
    embed.add_field(name="pause", value="Pausar la canción que está sonando")
    embed.add_field(name="resume", value="Reiniciar canción")
    embed.add_field(name="saltar", value="Pa saltar la canción ps")
    embed.add_field(
        name="chao", value="Para sacar a la parcera del canal de voz")
    await channel.send(content=None, embed=embed)
