from asyncore import loop
import random
import time
import discord
from discord.ext import commands

tostop = 0

intents = discord.Intents.all()

TOKEN = "MTA0NDYxODY0MTU4MjMzODA2OQ.G5SUXL.F1bUFjklNowSXPAuXAykXYpFE-mY9Wb-nOWPGo"
rh = commands.Bot(command_prefix=".", intents=intents)


def randnum(fname):
  lines = open(fname).read().splitlines()
  return random.choice(lines)


@rh.event
async def on_ready():
  print(f"Connected to {rh.user}")
  print(f"Bot ID : {rh.user.id}")


allowed = ["790662380052283444"]


@rh.command()
async def stop(ctx):
  global tostop
  if ctx.author.id == 790662380052283444 or ctx.author.id == 743431588599038003:
    tostop += 1
    await ctx.reply("**stopping pfps**")
  else:
    await ctx.reply("unauthorised")


@rh.command()
async def sendpfps(ctx):
  global tostop
  if ctx.author.id == 790662380052283444 or ctx.author.id == 743431588599038003: #kindly change the id names to your id's.
    tostop = 0
    await ctx.reply("**Sending pfps**")
    while tostop == 0:

      embed = discord.Embed(title=f"TITLE", description="a description", color=0x6509f5)
      embed.set_image(url=randnum('scraped.txt'))
      embed.set_footer(text="discord.gg/")
      await ctx.send(embed=embed)
      time.sleep(3)
  else:
    await ctx.send("unauthorised")


rh.run(TOKEN)
