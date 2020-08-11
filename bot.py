import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')

# ! comment to use custom help command
client.remove_command('help')

# * get env var
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# on_ready event
@client.event
async def on_ready():
    # change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Dota 2'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot is ready!')

# error event
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send('ngawur gak ada command kek gitu')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="List command bot:", description="semua command pake prefix '.' <= (titik)", color=0xb63b24)
    embed.add_field(name=".[build]", value="liat source code bot", inline=False)
    embed.add_field(name=".[ping]", value="nge ping host bot", inline=False)
    embed.add_field(name=".[kerang | k] <pertanyaan>", value="nanya kerang ajaib", inline=False)
    embed.add_field(name=".[flip]", value="lembar koin", inline=False)
    embed.add_field(name=".[roll] <low, default=0> <high, default=100>", value="roll dadu", inline=False)
    # embed.set_footer(name="dah gitu aja")
    await ctx.send(embed=embed)

@client.command()
async def build(ctx):
    await ctx.send(f"```author: rafi\nrepo: https://github.com/segi3/ya-bot-py```")

# load all cogs
for filename in os.listdir('./cogs'):
    if filename == 'music.py':
        print("music will not be loaded")
        continue
    elif filename == 'help.py':
        print("using default help command") #default command is in server cog
        continue
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ.get("TOKEN", None))