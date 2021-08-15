import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
  print("this bot is online")

@client.command()
async def hello(ctx):
  await ctx.send("Hey")

client.run("Your Discord Token")