import discord
from discord.ext import commands

description = "SHITPOST MACHINE 3000"

bot = commands.Bot(command_prefix="--", description=description)


@bot.event
async def on_ready():
    print("Ready to shitpost")

@bot.command()
async def shitpost(ctx):
    with open("input.txt", 'r') as f:
        for line in f:
            if line == "\n":
                continue
            else:
                await ctx.guild.create_voice_channel(line)

    await ctx.send("Done")        
    
bot.run("")
