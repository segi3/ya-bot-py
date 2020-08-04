import discord
import re
from discord.ext import commands

class Chatroom(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---------- events ----------
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        elif message.content.startswith('.'):
            return

        regx_ay = re.compile('(a|y)*$')
        regx_AY = re.compile('(A|Y)*$')

        if "ay" in message.content and regx_ay.match(message.content):
            # print("ay")
            ac = message.content.count("a") + 1
            yc = message.content.count("y") + 2
            msg_out = ''
            for i in range(ac):
                msg_out += 'a'
            for i in range(yc):
                msg_out += 'y'
            
            print(f'{msg_out}')
            await message.channel.send(f'{msg_out}')

        elif "AY" in message.content and regx_AY.match(message.content):
            # print("AY")
            ac = message.content.count("A") + 1
            yc = message.content.count("Y") + 2
            msg_out = ''
            for i in range(ac):
                msg_out += 'A'
            for i in range(yc):
                msg_out += 'Y'
            
            print(f'{msg_out}')
            await message.channel.send(f'{msg_out}')

        else:
            print('bukan ay AY')


    # ---------- commands ----------

    # clear messages command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount+1)

    # ---------- error handling ----------

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('specify amount of messages')


def setup(client):
    client.add_cog(Chatroom(client))