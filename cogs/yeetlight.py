import discord
from discord.ext import commands
import random
import asyncio

from yeelight import Bulb, LightType

class Yeetlight(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.bulb = Bulb("192.168.1.9")
        self.acceptInput = True
        self.isTimeout = False
    
    @commands.command(hidden=True, aliases=['yeeac'])
    async def accept_input(self, ctx, boolAccept=True):
        print(boolAccept)
        author = ctx.message.author
        if str(author) == 'YABOI#2205':
            if boolAccept:
                self.acceptInput = boolAccept
            else:
                self.acceptInput = boolAccept
        
        print("boolaccept: " + str(boolAccept))
    
    @commands.command(aliases=['lamp'])
    async def lampu(self, ctx, command, arg1=None):

        if command == 'isAccepting' or command == 'isAcceptingCommands':
            if self.acceptInput:
                await ctx.send('yes')
            else:
                await ctx.send('no')
        
        elif command == 'info':
            embd = discord.Embed(title='Info pake lampu', description='', color=0xb63b24)
            embd.add_field(name='`.lampu info`', value='gimana cara make command lampu', inline=False)
            embd.add_field(name='`.lampu isAcceptingCommands`', value='buat ngecek bot nya pengen di ganggu untuk ganti lampu atau engga', inline=False)
            embd.add_field(name='`.lampu isTimeout`', value='buat ngecek masih capek atau engga bot nya', inline=False)
            embd.add_field(name='`.lampu toggle`', value='mati/nyala lampu, tidak sembarang orang bisa ngejalanin ini', inline=False)
            
            embd.add_field(name='`.lampu setColor [warna]`', value='ganti warna, untuk `[warna]` nya bisa pake kode hex # atau warna premade', inline=False)
            embd.add_field(name='`.lampu preColor`', value='list warna yg premade', inline=False)

            embd.add_field(name='`.lampu setBright [level]`', value='nambah/ngurang terang, untuk `[level]` nya harus antara 0 sama 100', inline=False)

            await ctx.send(embed=embd)

        elif command == 'preColor':
            embd = discord.Embed(title='warna pre', description='red green blue turqoise yellow orange pink')
            await ctx.send(embed=embd)
        
        elif command == 'isTimeout':
            if self.isTimeout:
                await ctx.send('yes')
            else:
                await ctx.send('no')

        elif command == 'toggle':
            print('masuk toggle')
            author = ctx.message.author
            # if str(author) == 'YABOI#2205':
            self.bulb.toggle()

        elif command == 'setColor':

            preColors = [
                ['red', 255, 0, 0],
                ['green', 0, 255, 0],
                ['blue', 0, 0, 255],
                ['turqoise', 175, 238, 238],
                ['yellow', 255, 224, 93],
                ['orange', 255, 150, 66],
                ['pink', 255, 224, 93]
            ]

            valid = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f',
                'A', 'B', 'C', 'D', 'E', 'F'
            ]

            if self.acceptInput:
                if len(arg1) == 7 and arg1[0] == '#' and all(char in valid for char in arg1):
                    print('masuk setColor hex')
                    if self.isTimeout == False:
                        self.isTimeout = True

                        red = int(arg1[1] + arg1[2], 16)
                        green = int(arg1[3] + arg1[4], 16)
                        blue = int(arg1[5] + arg1[6], 16)

                        if red <= 0 and green <= 0 and blue <= 0:
                            print('no item')
                            return
                        
                        self.bulb.set_rgb(
                            red,
                            green,
                            blue)
                        
                        await asyncio.sleep(1)
                        await ctx.send(f'warna lampu berhasil diganti menjadi warna **{arg1}**')
                        self.isTimeout = False
                    else:
                        await ctx.send('timeout tunggu beberapa detik')

                elif any(arg1 in color for color in preColors):
                    print('masuk setColor premade ')
                    colorC = next(c for c in preColors if c[0] == arg1)
                    print(colorC)
                    # print(arg1 + colorC[1] + colorC[2] + colorC[3])
                    if self.isTimeout == False:
                        self.isTimeout = True

                        self.bulb.set_rgb(
                            colorC[1],
                            colorC[2],
                            colorC[3])
                        await asyncio.sleep(1)
                        await ctx.send(f'warna lampu berhasil diganti menjadi warna **{arg1}**')
                        self.isTimeout = False
                    else:
                        await ctx.send('timeout tunggu beberapa detik')

                else:
                    await ctx.send('warna tidak ditemukannnn')
            else:
                await ctx.send('lampu sedang tidak menerima input')
        
        elif command == 'setBrightness' or command == 'setBright':
           
            bright_level = int(arg1)
            if self.acceptInput:
                if bright_level >= 0 and bright_level <= 100:

                    if self.isTimeout == False:
                        self.isTimeout = True

                        self.bulb.set_brightness(bright_level)

                        await asyncio.sleep(1)
                        self.isTimeout = False
                        await ctx.send(f'brightness lampu berhasil diubah menjadi **{bright_level}%**')
                        
                    else:
                        await ctx.send('timeout tunggu beberapa detik')
                else:
                    await ctx.send('brightness harus 0<=n<=100')
            else:
                await ctx.send('lampu sedang tidak menerima input')
        
        else:
            await ctx.send('command tak dikenal :(')

        
    
    # @commands.command()
    # async def


    


def setup(client):
    client.add_cog(Yeetlight(client))