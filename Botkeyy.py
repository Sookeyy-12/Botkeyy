import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game("!helpme"))

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)
        
extensions = ['cogs.HelpCommands',
              'cogs.OnMessage',
              'cogs.BotCommands']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
        
bot.run(os.getenv('DISCORD_TOKEN'))

