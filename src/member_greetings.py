from random import choice

from discord import Member, TextChannel, Client
from utils import get_channel_id

GAYS = [
    "juansu01",
    "notguy.2",
    "jfgrivas",
    ".edwarto",
    "maxwell527",
    "alnair7337",
    "patataconesquizofrenia"
]

HETEROS = [
    "makiabelicos",
    "_bleisz",
    "dolphinvz",
    "elreydelamontana",
    "thegameroz"
]

MESSAGES_BY_NAME = {
    "fran": [
        "Ay, llegó mi parcera la más longeva",
        "Llego la zpa menos venenosa",
        "Alguien que la jubile porfaa",
        "Llegó la más reina",
        "La parcera más explota piñas",
        "Qn pa Ow amigaaa"
    ],
    "mustfa": [
        "Entró la parcera más dibujista",
        "Mi parcera, la más adicta a Poppy",
        "ora, cuéntame eso de los backroom mora",
        "Llegó la más comendiante, totaaal"
    ],
    "bto": [
        "Ya vino esta zpa a hablar del inge",
        "Mi amiga, la hetero lover",
        "Saquen a esa zpa trolla",
        "La más explotadora de piñas"
    ],
    "san": [
        "Mi amiga la más pantalonistaaa",
        "Qn pa escuchar a los embolatados",
        "Qn pa Ow amigaaa",
        "Mi amiga la menos capitalista"
    ],
    "gays": [
        "Llegó la parcera que más me pide popper totaaal",
        "Amiga tire popper",
        "Qn pa poner guaracha",
        "Ay, meras ganas de pipí, cierto?",
        "Llegó mi parcera la más activa",
        "Llegó mi parcera la más aguantadora",
        "Ay, y esta versátil?"
    ],
    "heteros": [
        "https://tenor.com/view/please-give-me-cock-korean-english-gif-14448929",
        "A ver ese paquete",
        "Fotodick o no pongo música",
        "Ya vamos a empezar a perder",
        "Sin pegarle a la pared pss",
        "Entra, pero sin hablar de fifa, bueno?"
    ]
}


def find_category_by_name(member: Member):
    username = member.name
    if username in HETEROS:
        return "heteros"
    if username in GAYS:
        return "gays"
    if username == "franciscoelias":
        return "fran"
    if username == "mustf_s":
        return "mustfa"
    if username == "san8210":
        return "san"
    if username == ".clorito":
        return "bto"

    return None


async def send_random_message(member: Member, client: Client):
    category = find_category_by_name(member)
    if not category:
        return
    if choice([1, 2]) == 1:
        return

    channel_id = get_channel_id(
        member.guild.channels, "General")
    channel = client.get_channel(channel_id)
    message_list = MESSAGES_BY_NAME[category]
    message = choice(message_list)
    await channel.send(f"{message} {member.mention}")
