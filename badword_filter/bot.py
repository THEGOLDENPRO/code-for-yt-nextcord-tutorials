import nextcord
from nextcord.ext import commands

import os
import bot_token
import json

client = commands.Bot(command_prefix="!")
os.chdir(os.getcwd())

@client.event
async def on_message(message):
    msg = message.content
    
    with open("words.json", "r+") as file:
        words_json = json.load(file)
        file.close()

    bad_words = words_json["bad_words"]

    broken_up_msg = msg.split()
    print(broken_up_msg)

    for bad_word in bad_words:
        if bad_word in broken_up_msg:
            channel = message.channel
            await message.delete()
            await channel.send("This word is not allowed!")

client.run(bot_token.TOKEN)