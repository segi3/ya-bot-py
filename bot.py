import random
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['status 1', 'status 2'])

# on_ready event
@client.event
async def on_ready():
    # change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Dota 2'))
    print('Bot is ready!')
<<<<<<< HEAD
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
=======
>>>>>>> b881099af1174e7fadc40a9c627381f6c4119eda

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

client.run('NzM5MzcwNDA2NjUzMTk4Mzk3.XyZeWQ.CJvBwdxtO0nNoRfO7GGoUyUcGxs')