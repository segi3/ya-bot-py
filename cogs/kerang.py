import discord
from discord.ext import commands
import random

class Kerang(commands.Cog, name="puja kerang ajaib"):

    def __init__(self, client):
        self.client = client
        self.weight_postive = 0.5
        self.weight_negative = 0.5
    
    # ---------- commands ----------

    @commands.command(hidden=True)
    async def test(self, ctx, *, question):
        answer = "answer"
        embed = discord.Embed(title=question, description=answer, color=0xb63b24)
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def pr_wg(self, ctx):
        print("masuk print weight")
        print(f'print pos {self.weight_postive}')
        print(f'print neg {self.weight_negative}')

    @commands.command(hidden=True)
    async def cg_wg(self, ctx, postive_in=0.5, negative_in=0.5):
        print("masuk set weight")
        print(f'set in pos {postive_in}')
        print(f'set in neg {negative_in}')
        self.weight_negative = negative_in
        self.weight_postive = postive_in
        print(f'set pos {self.weight_postive}')
        print(f'set neg {self.weight_negative}')

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

        positive_responses = [
            "pastinya",
            "udah pasi gitu",
            "udah darisananya juga gitu",
            "iyala, jelas",
            "yang aku liat sih iya",
            "hmm bisa jadi",
            "keliatannya gitu",
            "ya",
            "sip",
            "yoi",
            "YOI BANGET BRO",
            "yessss",
            "akulah segitiga",
            "petunjuk petunjuk ku mengarah ke jawaban iya",
        ]

        negative_responses = [
            "coba lagi",
            "YAKALI ANJIR WKWKWKWK",
            "pertanyaan laen",
            "gak mau ngasih tau",
            "hmm jawab engga ya",
            "tidak bisa diprediksi",
            "tolong fokus terus tanya lagi",
            "jangan berharap",
            "jawabanku tidak",
            "kata intel enggak",
            "keliatannya sih enggak",
            "tidak",
            "nope",
            "sama sekali tidak"
        ]

        if question in mancing_mania:
            await ctx.send('MANTAP')

        possible_response = ["positive", "negative"]
        weight = [self.weight_postive, self.weight_negative]

        print("masuk kerang")
        answer_tone = random.choices(possible_response, weights=weight, k=1)
        if answer_tone[0] == "positive":
            print("postive")
            embed = discord.Embed(title=question, description=random.choice(positive_responses), color=0xb63b24)
            await ctx.send(embed=embed)
        elif answer_tone[0] == "negative":
            print("negative")
            embed = discord.Embed(title=question, description=random.choice(negative_responses), color=0xb63b24)
            await ctx.send(embed=embed) 

    @kerang.error
    async def kerang_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('jangan lupa kasih pertanyaan. `[kerang|k] <pertanyaan>`')

def setup(client):
    client.add_cog(Kerang(client))