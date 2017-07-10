import discord
from discord.ext.commands import Bot
from discord.ext import commands
from config import TOKEN

Client = discord.Client()
bot_prefix= "?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def Bling(ctx):
    await client.say("Blowe!")

client.run(TOKEN)