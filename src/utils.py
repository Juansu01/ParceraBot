import yt_dlp


async def search_song(client, amount, song, get_url=False):
    info = await client.loop.run_in_executor(
        None,
        lambda: yt_dlp.YoutubeDL(
            {"format": "bestaudio",
             "quiet": True
             }
        ).extract_info(f"ytsearch{amount}:{song}",
                       download=False,
                       ie_key="YoutubeSearch"))
    for entry in info["entries"]:
        if entry.get("webpage_url"):
            return entry["webpage_url"]


def get_channel_id(channels, name):
    """
    Takes in a list of channels to find the channel
    that matches the name argument.
    """
    for channel in channels:
        if channel.name.lower() == name.lower():
            return channel.id

    return None
