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

@client.command(aliases=['kerang', 'ka', 'k'])
async def kerang_ajaib(ctx, *, question):
    mancing_mania = [
        'mancing mania',
        'mancing mania?',
        'Mancing mania',
        'Mancing mania?',
        'MANCING MANIA',
        'MANCING MANIA?'
    ]
    responses = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

    if question in mancing_mania:
        await ctx.send('MANTAP')
    else:
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


#load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ.get("TOKEN", None))