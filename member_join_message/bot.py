import nextcord
from nextcord.ext import commands

import bot_token

intents = nextcord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        msg = f"Welcome {member.mention} to {guild.name}"
        await guild.system_channel.send(msg)

client.run(bot_token.TOKEN)