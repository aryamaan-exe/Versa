import discord
from discord.ext import commands
import random, asyncio

token = list(open("token.txt"))[0]
client = commands.Bot(command_prefix="/")
client.remove_command('help')
responses = list(open("8ball.txt"))
fresponses = list(open("fortune.txt"))

@client.event
async def on_ready():
    print("Ready!")

@client.command(aliases=["tutorial", "commands", "allcommands"])
async def help(ctx):
    e = discord.Embed(title="List of Commands", color=0x00ff00, footer="Wow, that was a lot to take in! I hope you remember this lol")
    e.add_field(
        name= "/help",
        value= "Sends this prompt"
    )
    e.add_field(
        name= "/ping",
        value= "Shows bot ping"
    )
    e.add_field(
        name= "/8ball, /_8ball <question>",
        value= "Ask and you shall receive... Funny responses! 🤣"
    )
    e.add_field(
        name= "/fortunecookie, /fort, /fortune",
        value= "Tells you some fortune (please don't take it seriously)"
    )
    e.add_field(
        name= "/cool, /coolmetre, /howcool",
        value= "Shows how cool you are. I hope you get more than 80%!"
    )
    e.add_field(
        name= "/evil, /evilmetre, /howevil",
        value= "Shows how R00D you are 😈. Please just get below 20% 😇"
    )
    e.add_field(
        name= "/die, /dice, /roll, /rolldie, /rolladie",
        value= "Unlike the number of aliases, this die actually has 6 faces! (Hey that rhymes)"
    )
    e.add_field(
        name= "/coin, /flip, /coinflip, /flipcoin, /flipacoin",
        value= "Honestly at this point you know what a coin is"
    )
    e.add_field(
        name= "/rahman",
        value= "The one and only!"
    )
    e.add_field(
        name= "/tungsten, /stupid, /tungstenisstupid",
        value= "The one and only... stupid person 😜"
    )

    await ctx.send(embed=e)

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency, 2)}ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    await ctx.send(random.choice(responses))

@client.command(aliases=["fortunecookie", "fort"])
async def fortune(ctx):
    await ctx.send(random.choice(fresponses))

@client.command(aliases=["cool", "coolmetre"])
async def howcool(ctx):
    coolness = random.randint(0, 100)
    s = f"{ctx.author[:-5]} is {coolness}% cool!"
    if coolness > 79:
        s += " Wow!"
    await ctx.send(s)

@client.command(aliases=["evil", "evilmetre"])
async def howevil(ctx):
    evilness = random.randint(0, 100)
    s = f"{ctx.author[:-5]} is {evilness}% evil!"
    if evilness > 79:
        s += " R00D!"
    await ctx.send(s)

@client.command(aliases=["roll", "rolldie", "rolladie", "dice"])
async def die(ctx):
    number = random.randint(0, 6)
    s = f"You rolled a {number} 😀 "
    if number > 5:
        s += " Awesome! Just don't get it thrice in a row. 😫"
    await ctx.send(s)

@client.command(aliases=["flip", "flipcoin", "coinflip", "flipacoin"])
async def coin(ctx):
    face = random.randint(0, 1)
    if face:
        face = "Heads"
    else:
        face = "Tails"
    s = f"{face}! I hope you won your bet 😉"
    await ctx.send(s)

@client.command()
async def rahman(ctx):
    await ctx.send("Rahman is awesome!")

@client.command(aliases=["stupid", "tungstenisstupid"])
async def tungsten(ctx):
    await ctx.send("Tungsten is a dum dum 🤣\n*cling clang*")

@client.command(aliases=["randomguy"])
async def choose(ctx):
    await ctx.send(f"{random.choice(ctx.guild.members).name}, I choose you!")

client.run(token)