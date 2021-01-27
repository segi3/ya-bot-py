import discord
import os
import base64
from os.path import join, dirname
from dotenv import load_dotenv
from discord.ext import commands

from github import Github
from pprint import pprint

# * get env var
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

class Build(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tok(self, ctx):
        token = os.environ.get("GITHUB", None)
        username = os.environ.get("GITHUB_USERNAME", None)
        password = os.environ.get("GITHUB_PASSWORD", None)
        g = Github(username, password)
        user = g.get_user()
        repo = g.get_repo("segi3/ya-bot-py")
        print(repo.full_name)

        for cmt in repo.get_commits():
            print(f'author: {cmt.author} / comment: {cmt.commit}')
            print(cmt.commit.get_comments())

def setup (client):
    client.add_cog(Build(client))