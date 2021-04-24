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
        embed.add_field(name="!botinfo", value="Info about me", inline=True)
        embed.add_field(name="!ownerinfo", value="Info about Sookeyy", inline=True)
        embed.add_field(name="!q \"Your Question\"", value="Ask a Y/N Question", inline=True)
        embed.add_field(name="!joke", value="A Joke", inline=True)
        embed.add_field(name="!cat", value="Do you like Cats?", inline=True)
        embed.add_field(name="!ping", value="Reacts Pong!", inline=True)
        embed.add_field(name="!pong", value="Reacts Ping!", inline=True)
        embed.add_field(name="!hello", value="Feeling lonely?", inline=True)
        embed.add_field(name="!meme", value="A random meme", inline=True)
        embed.add_field(name="!guess", value="Play the number guessing game!", inline=True)
        embed.add_field(name="!discord", value="Join the Bot's Official Discord and share your views!", inline=True)
        embed.add_field(name="!github", value="Check out my GitHub", inline=True)
        embed.add_field(name="!spam", value="use in the format !spam <times> <message> eg. !spam 3 sup bro", inline=True)
        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommands(bot))