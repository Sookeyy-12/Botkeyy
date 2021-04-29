import discord
from discord.ext import commands

class InfoCommands(commands.Cog):
    """ Info about Bot and Owner """
    def __init__(self, bot):
        self.bot = bot
    
    # Bot Info Command
    @commands.command()
    async def botinfo(self, ctx):
        """ Information about Bot """
        await ctx.channel.send("""**__Bot v1.7.7__**
**Updates:** Added better Help Command (Thanks to Rachit)
**Info:** *Botkeyy is coded in Python by Sookeyy#0465*""")

    # Owner Info Command
    @commands.command()
    async def ownerinfo(self, ctx):
        """ Owner's GitHub """
        await ctx.channel.send("https://github.com/Sookeyy-12")
    
    # Discord Command
    @commands.command()
    async def discord(self, ctx):
        """ Bot's Official Discord Server """
        await ctx.channel.send('https://discord.gg/RKkg7EyD43')

    # GitHub Command
    @commands.command()
    async def github(self, ctx):
        """ Owner's GitHub """
        await ctx.channel.send('https://github.com/Sookeyy-12')

def setup(bot):
    bot.add_cog(InfoCommands(bot))