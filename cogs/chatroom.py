import discord
import re
from discord.ext import commands
import asyncio

class Chatroom(commands.Cog):
    """
    Chatroom Description
    """

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
        elif "segitiga" in message.content:
            emoji = '\U0001F53A'
            # or '\U0001f44d' or '👍'
            await message.add_reaction(emoji)
        elif "-p" in message.content:
            music_ch = discord.utils.get(message.guild.text_channels, name="🎵music-command")
            # music_ch = self.client.get_channel(361494244919083021)

            # if message.channel != music_ch:
            #     warning_msg = await message.channel.send(f"puter music di {music_ch.mention}, deleting in 3secs")
            #     await asyncio.sleep(3)
            #     await message.delete()
            #     await warning_msg.delete()
            
            # for channel in channels:
            #     if channel.name != "test_channel":
            #         print("haromm")
            #     else:
            #         continue
            #     print(channel.name)
           
        else:
            print('bukan ay AY')


    # ---------- commands ----------

    @commands.command(hidden=True)
    async def reply(self, ctx, *, message):
        channel = self.client.get_channel(762984237434535936)
        await channel.send(f'{message}')

    @commands.command(hidden=True)
    async def ms(self, ctx, *, message):
        print(f'command reply, msg:{message}')
        channel = self.client.get_channel(696017083154038784)
        await channel.send(f'{message}')

    # clear messages command
    @commands.command(hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount+1)
    
    # get channel
    @commands.command(hidden=True)
    async def where(self, ctx):
        message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention}'
        await ctx.send(message)
        # await ctx.message.author.send(message) # dm yang manggil command

    # get all channel list
    @commands.command(hidden=True, aliases=['lc'])
    async def list_channel(self, ctx):
        for guild in self.client.guilds:
            print(guild.name)
            if guild == ctx.message.guild:

                message = 'text channels:\n'
                embed = discord.Embed(title="Text channel:", description="", color=0xb63b24)
                for channel in guild.text_channels:
                    message += f'{channel.mention} - {channel.topic}\n'
                    embed.add_field(name=f"{channel.name}", value=f"{channel.mention} - {channel.topic}", inline=False)
                    print(channel.name)
                
                await ctx.send(message)
                await ctx.send(embed=embed)
            else:
                continue

    # ---------- error handling ----------

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('specify amount of messages')


def setup(client):
    client.add_cog(Chatroom(client))