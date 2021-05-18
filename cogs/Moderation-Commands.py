import discord
from discord.ext import commands

class ModerationCommands(commands.Cog):
    """Commands for Moderation (Can only be used by Sookeyy)"""
    def __init__(self, bot):
        self.bot = bot

    # Delete Message
    @commands.command()
    async def expunge(self, ctx, message_id=None):
        """Delete the Specified Message"""
        if message_id == None:
            await ctx.message.delete()
        if ctx.author.id == 456019145792815114:
            await ctx.message.delete()
            msg = await ctx.channel.fetch_message(message_id)
            await msg.delete()
        else:
            await ctx.send('Sorry, you don\'t have the permission to use that command.')






def setup(bot):
    bot.add_cog(ModerationCommands(bot))
