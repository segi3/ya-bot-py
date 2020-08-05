import discord
from discord.ext import commands
import random

class Kerang(commands.Cog, name="puja kerang ajaib"):

    def __init__(self, client):
        self.client = client
    
    # ---------- commands ----------

    @commands.command(hidden=True)
    async def test(self, ctx, *, question):
        answer = "answer"
        embed = discord.Embed(title=question, description=answer, color=0xb63b24)
        await ctx.send(embed=embed)

    @commands.command(brief="=> tanya kerang ajaib", description="tanya kerang ajaib", aliases=['k'])
    async def kerang(self, ctx, *, question):
        mancing_mania = [
            'mancing mania',
            'mancing mania?',
            'Mancing mania',
            'Mancing mania?',
            'MANCING MANIA',
            'MANCING MANIA?'
        ]
        responses = [
            "pastinya",
            "udah pasi gitu",
            "udah darisananya juga gitu",
            "iya, jelas",
            "yang aku liat sih, iya",
            "hmm bisa jadi",
            "keliatannya gitu",
            "ya",
            "petunjuk petunjuk ku mengarah ke jawaban iya",
            "coba lagi",
            "pertanyaan laen",
            "gak mau ngasih tau",
            "tidak bisa diprediksi",
            "tolong fokus terus tanya lagi",
            "jangan berharap",
            "jawabanku tidak",
            "kata intel enggak",
            "tidak terlihat baik",
            "tidak",
            "sama sekali tidak"]

        if question in mancing_mania:
            await ctx.send('MANTAP')
        else:
            embed = discord.Embed(title=question, description=random.choice(responses), color=0xb63b24)
            await ctx.send(embed=embed)
            # await ctx.send(f'`{question}`\n{random.choice(responses)}')

    @kerang.error
    async def kerang_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('jangan lupa kasih pertanyaan. `[kerang|k] <pertanyaan>`')

def setup(client):
    client.add_cog(Kerang(client))