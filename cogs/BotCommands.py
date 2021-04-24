import discord
from discord.ext import commands
import random
import json
import requests 
import os

x = random.randint(0,1)     # for question command

# Joke Api
def get_joke():
    response = requests.get(os.getenv('JOKE_API'))
    json_data = json.loads(response.text)
    if json_data['type'] == "single":
        joke = json_data['joke']
    else:
        joke = json_data['setup'] + " " + json_data['delivery']
    return(joke)

# Meme Api
def get_meme():
    response = requests.get(os.getenv('MEME_API'))
    json_data = json.loads(response.text)
    if json_data['nsfw'] == True and json_data['spoiler'] == True:
        pass
    else:
        meme = json_data['url']
    return(meme)

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.message.channel.send("Pong!")

    # Pong command
    @commands.command()	
    async def pong(self, ctx):
        await ctx.channel.send("Ping!")

    # Hello command
    @commands.command()
    async def hello(self, ctx):
        await ctx.channel.send("Hello! :wave:")
    
    # Bot Info Command
    @commands.command()
    async def botinfo(self, ctx):
        await ctx.channel.send("Am just a shitty BOT created by Sookeyy...")

    # Owner Info Command
    @commands.command()
    async def ownerinfo(self, ctx):
        await ctx.channel.send("https://github.com/Sookeyy-12")

    # Cat
    @commands.command()
    async def cat(self, ctx):
        await ctx.channel.send('ᓚᘏᗢᓓ ◯')

    # Joke Command
    @commands.command()
    async def joke(self, ctx):
        joke = get_joke()
        await ctx.channel.send(joke)

    # Question Command
    @commands.command()
    async def q(self, ctx):
        list1 = ['yes', 'no']
        await ctx.channel.send(list1[x])

    # Meme Command
    @commands.command()
    async def meme(self, ctx):
        meme = get_meme()
        await ctx.channel.send(meme)

    # Discord Command
    @commands.command()
    async def discord(self, ctx):
        await ctx.channel.send('https://discord.gg/RKkg7EyD43')

    # GitHub Command
    @commands.command()
    async def github(self, ctx):
        await ctx.channel.send('https://github.com/Sookeyy-12')

    # Spam Command
    @commands.command()
    async def spam(self, ctx, n, *, sentence):
        if int(n) <= 30:
            for i in range(int(n)):
                await ctx.channel.send(sentence)
        elif int(n) > 30:
            await ctx.channel.send('Too big, please input less than 30.')  
        else:
            pass

def setup(bot):
    bot.add_cog(BotCommands(bot))