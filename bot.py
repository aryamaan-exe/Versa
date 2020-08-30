import discord
from discord.ext import commands
import random, asyncio, json

token = list(open("token.txt"))[0]
responses = list(open("8ball.txt"))
fresponses = list(open("fortune.txt"))
jokes = list(open("jokes.txt"))

def get_prefix(client, message):
    with open("prefixes.json") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print("Ready!")
    
@client.event
async def on_guild_join(guild):
    with open("prefixes.json") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "-"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefixes.json") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_message(message):
    if message.content == "<@748739858091999363>":
        channel = message.channel
        await channel.send(f"Hi! My prefix for this guild is {get_prefix(client, message)}")
    await client.process_commands(message)

@commands.guild_only()
@client.command(aliases=["setprefix", "versaprefix"])
@commands.has_permissions(administrator=True)
async def prefix(ctx, *, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)
    
    await ctx.send("Done!")

@commands.guild_only()
@client.command(aliases=["tutorial", "commands", "allcommands"])
async def help(ctx):
    e = discord.Embed(title="List of Commands", color=0x00ff00)
    e.add_field(
        name= "-help",
        value= "Sends this prompt"
    )
    e.add_field(
        name= "-ping",
        value= "Shows bot ping"
    )
    e.add_field(
        name= "-8ball, -_8ball <question>",
        value= "Ask and you shall receive... Funny responses! 🤣"
    )
    e.add_field(
        name= "-fortunecookie, -fort, -fortune",
        value= "Tells you some fortune (please don't take it seriously)"
    )
    e.add_field(
        name= "-cool, -coolmetre, -howcool",
        value= "Shows how cool you are. I hope you get more than 80%!"
    )
    e.add_field(
        name= "-evil, -evilmetre, -howevil",
        value= "Shows how R00D you are 😈. Please just get below 20% 😇"
    )
    e.add_field(
        name= "-die, -dice, -roll, -rolldie, -rolladie",
        value= "Unlike the number of aliases, this die actually has 6 faces! (Hey that rhymes)"
    )
    e.add_field(
        name= "-coin, -flip, -coinflip, -flipcoin, -flipacoin",
        value= "Honestly at this point you know what a coin is"
    )
    e.add_field(
        name="-choose, -randomguy",
        value= "Choose a random Poké— I mean human"
    )
    e.add_field(
        name= "-tungsten, -stupid, -tungstenisstupid",
        value= "The one and only... stupid person 😜"
    )
    e.add_field(name="-prefix, -setprefix, -versaprefix", 
    value="Change the prefix of the bot. You need to be an admin to do so (take note, peasants)")
    e.add_field(name="-joke, -tellmeajoke",
    value="Tells you a joke from a random collection of Tungsten's bad dad jokes.")
    e.set_footer(text="Wow, that was a lot to take in! I hope you remember this lol")

    await ctx.author.send(embed=e)
    await ctx.author.send("Note that - is the default prefix. Ping @Versa#3702 to get the prefix for your guild (although you already know the prefix cuz you used this command)")
    await ctx.send("Sent you a DM with the info!")

@commands.guild_only()
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency, 2)}ms")

@commands.guild_only()
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    await ctx.send(random.choice(responses))

@commands.guild_only()
@client.command(aliases=["fortunecookie", "fort"])
async def fortune(ctx):
    await ctx.send(random.choice(fresponses))

@commands.guild_only()
@client.command(aliases=["cool", "coolmetre"])
async def howcool(ctx):
    coolness = random.randint(0, 100)
    s = f"{str(ctx.author)[:-5]} is {coolness}% cool!"
    if coolness > 79:
        s += " Wow!"
    await ctx.send(s)

@commands.guild_only()
@client.command(aliases=["evil", "evilmetre"])
async def howevil(ctx):
    evilness = random.randint(0, 100)
    s = f"{str(ctx.author)[:-5]} is {evilness}% evil!"
    if evilness > 79:
        s += " R00D!"
    await ctx.send(s)

@commands.guild_only()
@client.command(aliases=["roll", "rolldie", "rolladie", "dice"])
async def die(ctx):
    number = random.randint(0, 6)
    s = f"You rolled a {number} 😀 "
    if number > 5:
        s += " Awesome! Just don't get it thrice in a row. 😫"
    await ctx.send(s)

@commands.guild_only()
@client.command(aliases=["flip", "flipcoin", "coinflip", "flipacoin"])
async def coin(ctx):
    face = random.randint(0, 1)
    if face:
        face = "Heads"
    else:
        face = "Tails"
    s = f"{face}! I hope you won your bet 😉"
    await ctx.send(s)

@commands.guild_only()
@client.command(aliases=["stupid", "tungstenisstupid"])
async def tungsten(ctx):
    await ctx.send("Tungsten is a dum dum 🤣\n*cling clang*")

@commands.guild_only()
@client.command(aliases=["randomguy"])
async def choose(ctx):
    await ctx.send(f"{random.choice(ctx.guild.members).name}, I choose you!")

@commands.guild_only()
@client.command(aliases=["tellmeajoke"])
async def joke(ctx):
    number = random.randrange(0, len(jokes)-1, 2)
    await ctx.send(jokes[number])
    await asyncio.sleep(2)
    await ctx.send(jokes[number+1])

client.run(token)
