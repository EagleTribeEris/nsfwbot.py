##This code is for Voltage Revolt bots.

@client.command()
async def nsfw(ctx):
    if ctx.channel.nsfw:
        ##NSFW content here. Replace this message with your code to be excecuted in discord NSFW channels
    else:
        await ctx.send("This command can only be used in a NSFW channel")
