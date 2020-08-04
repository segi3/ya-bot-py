import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---------- commands ----------
    @commands.command()
    async def playlist(self, ctx, playlist_name):
        await ctx.send('-p honne day 1')

def setup(client):
    client.add_cog(Music(client))