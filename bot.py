import random
import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')

# * get env var
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# on_ready event
@client.event
async def on_ready():
    # change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Dota 2'))
    print('Bot is ready!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

# error event
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('invalid command')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes',
                'Nope']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


#load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ.get("TOKEN"))