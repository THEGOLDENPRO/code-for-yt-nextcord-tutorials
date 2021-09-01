import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')

bot.run('ha ha, no token for you')