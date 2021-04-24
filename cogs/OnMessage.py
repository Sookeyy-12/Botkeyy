import discord
import random
import asyncio
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
        if 'cat' in message.content:
            await message.channel.send('Did someone say cats? ᓚᘏᗢ')


        # Guessing game
        if message.content.startswith('!guess'):
            await message.channel.send('Guess a Number from 0 to 10. Messaging in between will cancle the game!')
            attempt = 0
            answer = random.randint(0,10)
            while True:
                attempt += 1
                try:
                    guess = await self.bot.wait_for('message')
                except asyncio.TimeoutError:
                    return await message.channel.send(f'Sorry, You took too long, it was {answer}.')
                if int(guess.content) < answer:
                    await message.channel.send('The number should be Bigger!')
                elif int(guess.content) > answer:
                    await message.channel.send('The number should be Smaller!')
                elif int(guess.content) == answer:
                    await message.channel.send(f'Bingo! You guessed the Number in {attempt} attempt(s)!')
                else:
                    return
                    break

def setup(bot):
    bot.add_cog(OnMessage(bot))
