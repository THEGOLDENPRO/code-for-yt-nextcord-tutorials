import nextcord
from nextcord.ext import commands

import bot_token

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is Happy and Ready!")

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Confirming", ephemeral=True)
        self.vaule = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Cancelling", ephemeral=True)
        self.vaule = False
        self.stop()

@client.command()
async def ask(ctx):
    view = Confirm()
    await ctx.send("Do you want to confirm somthing.", view=view)

    await view.wait()

    if not view.value == None:
        print("Timed Out")
    if view.value == True:
        print("Comfirmed")
    if view.value == False:
        print("Cancelled")

client.run(bot_token.TOKEN)