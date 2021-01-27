import discord
from discord.ext import commands
import random

class Gamble(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def flip(self, ctx):
        coin = ['Burung', 'Angka']
        author = ctx.message.author
        message = f'{author.mention} flipped `{random.choice(coin)}`'
        await ctx.send(message)
    
    @commands.command()
    async def roll(self, ctx, high_ = 100, low_= 0):
        author = ctx.message.author
        message = f'{author.mention} rolled [{high_}-{low_}]: `{random.randint(low_, high_)}`'
        await ctx.send(message)


def setup(client):
    client.add_cog(Gamble(client))