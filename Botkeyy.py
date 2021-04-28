import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from pretty_help import DefaultMenu, PrettyHelp

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

menu = DefaultMenu('◀️', '▶️', '❌')
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.green())

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("!help"))

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)
        
extensions = ['cogs.infoCommands','cogs.OnMessage','cogs.utilityCommands','cogs.BotCommands','cogs.funCommands']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
        
bot.run(os.getenv('DISCORD_TOKEN'))

