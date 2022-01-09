import discord
from discord.ext import commands
import random
from cogs.packages.jokes import get_joke        # importing get_joke from packages
from cogs.packages.memes import get_meme        # importing get_meme from packages
from cogs.packages.quotes import get_quote      # importing get_quote from packages
import time

bot = commands.Bot(command_prefix="!")  # define bot

class BotCommands(commands.Cog):
    """ General Bot Commands """
    def __init__(self, bot):
        self.bot = bot

    # Pijja command
    @commands.command()
    async def pijja(self, ctx):
        """ sends rakshu pijja emoji """
        await ctx.channel.send("<:rakshu_pijja3:912246061790273546>")
        
    # Dumbo command
    @commands.command()
    async def dumbo(self, ctx):
        """ sends rakshu dumbo emoji """
        await ctx.channel.send("<:rakshu_dumbo:835752792588156928>")
        
    # Bigeyes command
    @commands.command()
    async def bigeyes(self, ctx):
        """ sends rakshu bigeyes emoji """
        await ctx.channel.send("<:rakshu_bigeyes:835747245231702066>")
        
    # Shrug command
    @commands.command()
    async def shrug(self, ctx):
        """ sends rakshu shrug emoji """
        await ctx.channel.send("<:rakshu_shrug:868151545680789555>")
        
    # Rage command
    @commands.command()
    async def rage(self, ctx):
        """ sends rakshu bigeyes emoji """
        await ctx.channel.send("<:rakshu_rage:836087210779738122>")
                
    # Amazed command
    @commands.command()
    async def rage(self, ctx):
        """ sends rakshu amazed emoji """
        await ctx.channel.send("<:rakshu_amazed:835503488083165205>")
        
     # Happy command
    @commands.command()
    async def pijja(self, ctx):
        """ sends rakshu happy emoji """
        await ctx.channel.send("<:rakshu_happy:835507548044001291>")
        
    # Sweat command
    @commands.command()
    async def pijja(self, ctx):
        """ sends rakshu sweat smile emoji """
        await ctx.channel.send("<:rakshu_sweat_smile:868076020878684192>") 
        
    # Partying command
    @commands.command()
    async def pijja(self, ctx):
        """ sends rakshu partying emoji """
        await ctx.channel.send("<:Rakshu_partying:878666695378628698>") 
        
        
       

    # Cat
    @commands.command()
    async def cat(self, ctx):
        """ Ya like Cats? """
        await ctx.channel.send('ᓚᘏᗢᓓ ◯')

    # Joke Command
    @commands.command()
    async def joke(self, ctx):
        """ Generates a random Joke """
        joke = get_joke()
        await ctx.channel.send(joke)

    # Question Command
    @commands.command()
    async def q(self, ctx):
        """ Ask a Y/N Question. Usage: !q <your y/n question> """
        x = random.randint(0,1)     # for question command
        list1 = ['yes', 'no']
        await ctx.channel.send(list1[x])

    # Meme Command
    @commands.command()
    async def meme(self, ctx):
        """ Generates a Random meme from r/memes """
        meme = get_meme()
        await ctx.channel.send(meme)

    # Quote Command
    @commands.command()
    async def quote(self, ctx):
        """ Generates a Random Famous Quote """
        quote = get_quote()
        await ctx.channel.send(quote)

    # Bot's Invite
    @commands.command()
    async def invite(self, ctx):
        """Invite the Bot to your Server!"""
        await ctx.channel.send('https://discord.com/api/oauth2/authorize?client_id=833751180760711189&permissions=8&scope=bot')

def setup(bot):
    bot.add_cog(BotCommands(bot))
