import discord
from discord.ext import commands
import random
from cogs.packages.jokes import get_joke        # importing get_joke from packages
from cogs.packages.memes import get_meme        # importing get_meme from packages
from cogs.packages.quotes import get_quote      # importing get_quote from packages
import time

bot = commands.Bot(command_prefix="!")  # define bot

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Hello command
    @commands.command()
    async def hello(self, ctx):
        """ Hello! """
        await ctx.channel.send("Hello! :wave:")

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
        x = random.randint(0,1)     # for question command
        list1 = ['yes', 'no']
        await ctx.channel.send(list1[x])

    # Meme Command
    @commands.command()
    async def meme(self, ctx):
        meme = get_meme()
        await ctx.channel.send(meme)

    # Quote Command
    @commands.command()
    async def quote(self, ctx):
        quote = get_quote()
        await ctx.channel.send(quote)


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