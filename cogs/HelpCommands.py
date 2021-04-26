import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help Command
    @commands.command()
    async def help(self, ctx):
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
        embed.add_field(name="!discord", value="Join the Bot's Official Discord and share your views!", inline=True)
        embed.add_field(name="!github", value="Check out my GitHub", inline=True)
        embed.add_field(name="!quote", value="Get a Famous random Quote", inline=True)
        embed.add_field(name="!rps", value="Play a game of Rock, Paper & Scissors.", inline=True)
        embed.add_field(name="!guess", value="Play the number guessing game! usage: ``!guess <min> <max>``", inline=False)
        embed.add_field(name="!spam", value="usage: ``!spam <amount> <your message>``", inline=False)
        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCommands(bot))