import discord
from discord.ext import commands
import random, asyncio

responses = list(open("8ball.txt"))
fresponses = list(open("fortune.txt"))
jokes = list(open("jokes.txt"))

class Rand(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # @commands.Cog.listener()
    @commands.guild_only()
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        await ctx.send(random.choice(responses))
    
    @commands.guild_only()
    @commands.command(aliases=["fortunecookie", "fort"])
    async def fortune(self, ctx):
        await ctx.send(random.choice(fresponses))
    
    @commands.guild_only()
    @commands.command(aliases=["cool", "coolmetre"])
    async def howcool(self, ctx):
        coolness = random.randint(0, 100)
        s = f"{str(ctx.author)[:-5]} is {coolness}% cool!"
        if coolness > 79:
            s += " Wow 😎"
        await ctx.send(s)
    
    @commands.guild_only()
    @commands.command(aliases=["evil", "evilmetre"])
    async def howevil(self, ctx):
        evilness = random.randint(0, 100)
        s = f"{str(ctx.author)[:-5]} is {evilness}% evil!"
        if evilness > 79:
            s += " R00D 😈"
        await ctx.send(s)

    @commands.guild_only()
    @commands.command(aliases=["roll", "rolldie", "rolladie", "dice"])
    async def die(self, ctx):
        number = random.randint(1, 6)
        s = f"You rolled a {number} 😀 "
        if number > 5:
            s += " Awesome! Just don't get it thrice in a row. 😫"
        await ctx.send(s)
    
    @commands.guild_only()
    @commands.command(aliases=["flip", "flipcoin", "coinflip", "flipacoin"])
    async def coin(self, ctx):
        face = random.randint(0, 1)
        if face:
            face = "Heads"
        else:
            face = "Tails"
        s = f"{face}! I hope you won your bet 😉"
        await ctx.send(s)
    
    @commands.guild_only()
    @commands.command(aliases=["tellmeajoke"])
    async def joke(self, ctx):
        number = random.randrange(0, len(jokes)-1, 2)
        await ctx.send(jokes[number])
        await asyncio.sleep(2)
        await ctx.send(jokes[number+1])
    @commands.guild_only()
    @commands.command(aliases=["randomguy"])
    async def choose(self, ctx):
        await ctx.send(f"{random.choice(ctx.guild.members).name}, I choose you!")

def setup(client):
    client.add_cog(Rand(client))
