from utils import get_channel_id
import random


async def leave_after_being_left_alone(member, before, client):
    if len(before.channel.members) > 1 or not client.voice_clients:
        return
    for voice_client in client.voice_clients:
        if voice_client.guild.id == before.channel.guild.id:
            channel_id = get_channel_id(
                member.guild.channels, "General")
            channel = client.get_channel(channel_id)
            if random.choice([1, 2, 3]) == 1:
                await channel.send(f"No {member.mention} dejándome sola :face_with_symbols_over_mouth:")
            await voice_client.disconnect()
