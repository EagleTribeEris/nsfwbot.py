import voltage
from voltage.ext import commands
import random
import asyncio
import aiohttp

client = commands.CommandsClient("!")

##NSFW Command Below

@client.command()
async def nsfw(ctx):
    if ctx.channel.nsfw:
        ##NSFW content here. Replace this message with your code to be excecuted in Revolt's NSFW channels
    else:
        await ctx.send("This command can only be used in a NSFW channel")





client.run("BOTTOKENHERE")
