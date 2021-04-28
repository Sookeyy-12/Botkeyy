import discord
import asyncio
from discord.ext import commands
import random

class funCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Guessing Game
    @commands.command()
    async def guess(self, ctx, x=None, y=None):
        if x is None or y is None :
            await ctx.channel.send('Please Provide a Range.')
        elif (int(y) - int(x)) > 1001:
            await ctx.channel.send('Range too big, Please Reduce the Range.')
        elif (int(y)-int(x)) <= 1001:
            await ctx.channel.send(f'Guess a Number from {int(x)} to {int(y)}.')
            answer = random.randint(int(x),int(y))
            attempt = 0
            while True:
                attempt += 1
                try:
                    guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10.0)
                except asyncio.TimeoutError:
                    return await ctx.channel.send(f'Sorry, You took too long, it was {answer}.')
                if int(attempt) == 15:
                    await ctx.channel.send(f'You took too many attempts, the answer was {answer}!')
                    break
                elif int(guess.content) < answer:
                    await ctx.channel.send('The Number should be Bigger!')
                elif int(guess.content) > answer:
                    await ctx.channel.send('The Number should be Smaller!')
                elif int(guess.content) == answer:
                    await ctx.channel.send(f'Bingo! You guess the number in {attempt} attempt(s)')
                    break
                    
    # Rock Paper Scissors
    @commands.command(name='playrps')
    async def rps(self, ctx):
        message = await ctx.channel.send('Choose one from Rock, Paper, Scissors')
        choices = ['🪨', '📄', '✂️']
        for choice in choices:
            await message.add_reaction(choice)
        answer = random.randint(0,2)
        bot_choice = choices[answer]
        reaction, user = await self.bot.wait_for('reaction_add', check= lambda r, u: u == ctx.author and r.message == message)
        if reaction.emoji == '🪨' and bot_choice == '✂️':
            await ctx.send(f'You Won! I chose {bot_choice}')
        elif reaction.emoji == '📄' and bot_choice == '🪨':
            await ctx.send(f'You Won! I chose {bot_choice}')
        elif reaction.emoji == '✂️' and bot_choice == '📄':
            await ctx.send(f'You Won! I chose {bot_choice}')
        elif reaction.emoji == bot_choice:
            await ctx.send(f'Its a Draw! I chose {bot_choice} too!')
        else:
            await ctx.send(f'You Lost... I chose {bot_choice}')

def setup(bot):
    bot.add_cog(funCommands(bot))