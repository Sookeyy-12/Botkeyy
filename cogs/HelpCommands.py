import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help Command
    @commands.command()
    async def helpme(self, ctx):
        embed=discord.Embed(title="Sookeyy - Github", url="https://github.com/Sookeyy-12", description='Come checkout my Github', color=discord.Color.random())
        embed.set_author(name = "Sookeyy#0465", url="https://github.com/Sookeyy-12", icon_url="https://i.imgur.com/vhrAZ7n.jpeg")
        embed.set_thumbnail(url="https://i.imgur.com/vhrAZ7n.jpeg")
        embed.add_field(name="!botinfo", value="Info about me", inline=False)
        embed.add_field(name="!ownerinfo", value="Info about Sookeyy", inline=False)
        embed.add_field(name="!q \"Your Question\"", value="Ask a Y/N Question", inline=False)
        embed.add_field(name="!joke", value="A Joke", inline=False)
        embed.add_field(name="!cat", value="Do you like Cats?", inline=False)
        embed.add_field(name="!ping", value="Reacts Pong!", inline=False)
        embed.add_field(name="!pong", value="Reacts Ping!", inline=False)
        embed.add_field(name="!hello", value="Feeling lonely?", inline=False)
        embed.add_field(name="!meme", value="A random 'clean' meme", inline=False)
        embed.add_field(name="!guess", value="Play the number guessing game!", inline=False)
        embed.add_field(name="!discord", value="Join the Bot's Official Discord and share your views!", inline=False)
        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommands(bot))