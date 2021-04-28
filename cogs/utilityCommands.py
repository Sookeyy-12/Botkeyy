import discord
from discord.ext import commands

class utilityCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # Ping command
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
        print(f'Ping {int(ping)}ms')

    # Pong command
    @commands.command()	
    async def pong(self, ctx):
        """ Ping! """
        before = time.monotonic()
        message = await ctx.send("Ping!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping!  `{int(ping)}ms`")
        print(f'Ping {int(ping)}ms')

def setup(bot):
    bot.add_cog(utilityCommands(bot))