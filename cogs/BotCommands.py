import discord
from discord.ext import commands
import random
import asyncio
from cogs.packages.jokes import get_joke        # importing get_joke from packages
from cogs.packages.memes import get_meme        # importing get_meme frmo packages

bot = commands.Bot(command_prefix="!")  # define bot

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.message.channel.send("Pong! {0}".format(round(self.bot.latency, 2)))

    # Pong command
    @commands.command()	
    async def pong(self, ctx):
        await ctx.channel.send("Ping! {0}".format(round(self.bot.latency, 2)))

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
        x = random.randint(0,1)     # for question command
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

    # Guessing Game
    @commands.command()
    async def guess(self, ctx, x=None, y=None):
        if x is None or y is None :
            await ctx.channel.send('Please Provide a Range.')
        elif (int(y) - int(x)) > 1001:
            await ctx.channel.send('Range too big, Please Reduce the Range.')
        elif (int(y)-int(x)) <= 1001:
            await ctx.channel.send(f'Guess a Number from {int(x)} to {int(y)}.')
            answer = random.randint(int(x),int(y))
            attempt = 0
            while True:
                attempt += 1
                try:
                    guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10.0)
                except asyncio.TimeoutError:
                    return await ctx.channel.send(f'Sorry, You took too long, it was {answer}.')
                if int(attempt) == 15:
                    await ctx.channel.send(f'You took too many attempts, the answer was {answer}!')
                    break
                elif int(guess.content) < answer:
                    await ctx.channel.send('The Number should be Bigger!')
                elif int(guess.content) > answer:
                    await ctx.channel.send('The Number should be Smaller!')
                elif int(guess.content) == answer:
                    await ctx.channel.send(f'Bingo! You guess the number in {attempt} attempt(s)')
                    break


def setup(bot):
    bot.add_cog(BotCommands(bot))