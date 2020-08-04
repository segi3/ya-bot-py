import discord
from discord.ext import commands

class Server(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---------- events ----------

    
    # on_member_join event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server')
    
    # on_member_remove event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server')

    
    # ---------- commands ----------

    # ping command
    @commands.command()
    async def ping(self, ctx):
        """ => PONG """
        await ctx.send(f'Pong! [{round(self.client.latency * 1000)}ms]')

    # kick command
    @commands.command(hidden=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'kicked {member.name}#{member.discriminator}')

    # ban command
    @commands.command(hidden=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.name}#{member.discriminator}')

    # unban command
    @commands.command(hidden=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(Server(client))