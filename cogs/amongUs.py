import discord
from discord.ext import commands
import asyncio

class amongUs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command(hidden=True, aliases=["mta"])
    @commands.has_permissions(administrator=True)
    async def muteall(self, ctx):

        mem = []
        message =''

        voice_channel = ctx.author.voice.channel

        for member in voice_channel.members:
            mem.append(member.nick)
            await member.edit(mute=True)
        
        maen_ch = self.client.get_channel(753912385768521830)

        for member in mem:
            message+=member + " "
        message+='muted'

        msg_mute = await maen_ch.send(f'{message}')
        await asyncio.sleep(5)
        await msg_mute.delete()

    @commands.command(hidden=True, aliases=["umta"])
    @commands.has_permissions(administrator=True)
    async def unmuteall(self, ctx):

        mem = []
        message =''

        voice_channel = ctx.author.voice.channel

        for member in voice_channel.members:
            mem.append(member.nick)
            await member.edit(mute=False)
        
        maen_ch = self.client.get_channel(753912385768521830)

        for member in mem:
            message+=member + " "
        message+='unmuted'
        
        msg_mute = await maen_ch.send(f'{message}')
        await asyncio.sleep(5)
        await msg_mute.delete()
        

def setup(client):
    client.add_cog(amongUs(client))