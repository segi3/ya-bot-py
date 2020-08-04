import discord
from discord.ext import commands

class _cogs(commands.Cog):

    def __init__(self, client):
        self.client = client

    # ---------- commands ----------

    # load cog file
    @commands.command(hidden=True)
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')

    # unload cog file
    @commands.command(hidden=True)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

    # reload cog file
    @commands.command(hidden=True)
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
    
def setup(client):
    client.add_cog(_cogs(client))