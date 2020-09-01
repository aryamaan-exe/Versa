import discord
from discord.ext import commands
import json

p = "prefixes.json"

class Other(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Tungsten"))
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open(p) as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "-"
        with open(p, "w") as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open(p) as f:
            prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open(p) as f:
            json.dump(prefixes, f, indent=4)


    @commands.guild_only()
    @commands.command(aliases=["setprefix", "versaprefix"])
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, *, prefix):
        with open(p, "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open(p, "w") as f:
            json.dump(prefixes, f)
        
        await ctx.send("Done!")
    
    @commands.guild_only()
    @commands.command(aliases=["tutorial", "commands", "allcommands"])
    async def help(self, ctx):
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
        e.add_field(
            name="-prefix, -setprefix, -versaprefix", 
            value="Change the prefix of the bot. You need to be an admin to do so (take note, peasants)"
        )
        e.add_field(
            name="-joke, -tellmeajoke",
            value="Tells you a joke from a random collection of Tungsten's bad dad jokes."
        )
        e.add_field(
            name="-track, -trackmessages",
            value="Track how many messages you've sent in all the servers Versa is in."
        )
        e.add_field(
            name="-lb, -leaderboard", 
            value="Show the global leaderboard of all the messages sent"
        )
        e.add_field(
            name="-msgbar, -messagebar <color>",
            value="Tungsten's favorite function! It shows a bar graph representation of -lb. You can have red, blue etc. as color, but I like to add hex values!"
        )
        e.add_field(
            name="-support <query>",
            value="Send your questions to the support server"
        )
        e.set_footer(text="Wow, that was a lot to take in! I hope you remember this lol")

        await ctx.author.send(embed=e)
        await ctx.author.send("Note that - is the default prefix. Ping @Versa#3702 to get the prefix for your guild (although you already know the prefix cuz you used this command)")
        await ctx.send("Sent you a DM with the info!")
    
    @commands.guild_only()
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.client.latency, 2)}ms")


    @commands.guild_only()
    @commands.command(aliases=["stupid", "tungstenisstupid"])
    async def tungsten(self, ctx):
        await ctx.send("Tungsten is a dum dum 🤣\n*cling clang*")

    @commands.guild_only()
    @commands.command()
    async def dmme(self, ctx, *, message):
        await ctx.author.send(message)
    
    @commands.command()
    async def support(self, ctx, *, query):
        channel = self.client.get_channel(749853278811979796)
        sup_server = self.client.get_guild(744795520408617041)
        footer = f"User ID is {ctx.author.id}. "
        if sup_server.get_member(ctx.author.id) == None:
            footer += "User not in support server."
        e = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} asks:", description=query, footer=footer, color=0x0000ff)
        await ctx.send("Your question has been sent to the support server. Versa is fun but respect the time of the helpers. You will be banned if your query is not, in fact, a query.")
        await channel.send(embed=e)

def setup(client):
    client.add_cog(Other(client))
