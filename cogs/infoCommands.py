import discord
from discord.ext import commands

class infoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Bot Info Command
    @commands.command()
    async def botinfo(self, ctx):
        await ctx.channel.send("""Bot v1.4.1.
        Botkeyy is coded in Python by Sookeyy#0465""")

    # Owner Info Command
    @commands.command()
    async def ownerinfo(self, ctx):
        await ctx.channel.send("https://github.com/Sookeyy-12")
    
    # Discord Command
    @commands.command()
    async def discord(self, ctx):
        await ctx.channel.send('https://discord.gg/RKkg7EyD43')

    # GitHub Command
    @commands.command()
    async def github(self, ctx):
        await ctx.channel.send('https://github.com/Sookeyy-12')

def setup(bot):
    bot.add_cog(infoCommands(bot))