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
