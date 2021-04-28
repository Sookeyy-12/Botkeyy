import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.bot: return

        # cat in the chat
        if 'cats' in message.content:
            await message.channel.send('Did someone say cats? ᓚᘏᗢ')

def setup(bot):
    bot.add_cog(OnMessage(bot))
