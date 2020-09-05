import discord
from discord.ext import commands
import json, random

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

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global sniped_message
        sniped_message = message
        global snipe_victim
        snipe_victim = message.author

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
        e.add_field(
            name="-dumb",
            value="Command made in 5 seconds due to request by a dumb person, this shows your level of dumbness (is that a word? gosh im so dumb)"
        )
        e.add_field(
            name="-dmme <something>",
            value="DMs you whatever you write. Please don't use this for bad things lol"
        )
        e.add_field(
            name="-snipe",
            value="Sometimes people just write bad stuff and delete it immediately after. THAT'S NOT HOW IT WORKS NOW BUDDY"
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
    async def dumb(self, ctx):
        await ctx.send(f"{ctx.author} is {random.randint(0, 100)}% dumb")

    @commands.guild_only()
    @commands.command()
    async def snipe(self, ctx):
        e = discord.Embed(
            title=f"{snipe_victim.name} said:",
            description=sniped_message.content,
            color=0x0000ff
        )
        await ctx.send(embed=e)
    
    @commands.guild_only()
    @commands.command()
    async def convert(self, ctx, *, dec):
        try:
            dec = int(dec)
            to_bin = bin(dec)[2:]
            to_hex = hex(dec)[2:]
            to_oct = oct(dec)[2:]
            await ctx.send(f"Decimal: `{dec}`\nBinary: `{to_bin}`\nHexadecimal: `{to_hex}`\nOctal: `{to_oct}`")
        except:
            await ctx.send("Invalid argument!")
    
    @commands.guild_only()
    @commands.command()
    async def frombin(self, ctx, *, n):
        try:
            dec = int(n, 2)
            to_bin = bin(dec)[2:]
            to_hex = hex(dec)[2:]
            to_oct = oct(dec)[2:]
            await ctx.send(f"Decimal: `{dec}`\nBinary: `{to_bin}`\nHexadecimal: `{to_hex}`\nOctal: `{to_oct}`")
        except:
            await ctx.send("Invalid argument!")
    
    @commands.guild_only()
    @commands.command(aliases=["fancytext"])
    async def fancy(self, ctx, *, text):
        all_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        all_fancy = "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘"
        all_fancy2 = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘"
        output = ""
        output2 = ""
        for char in text:
            if char in all_text:
                output += all_fancy[all_text.index(char)]
                output2 += all_fancy2[all_text.index(char)]
            else:
                output += char
                output2 += char
            
        await ctx.send(f"{output}\n{output2}")
    
    @commands.guild_only()
    @commands.command(aliases=["upsidedown", "updown"])
    async def upsidedowntext(self, ctx, *, text):
        all_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790`1234567890-=~!@#$%^&()_+[]\;',./?><\":|}{+_"
        all_up = "‾+}{|:,,><¿/˙',;\[]+‾()⅋^%$#@¡~=-068ㄥ9ϛㄣƐᄅƖ,06ㄥ9ϛㄣƐᄅƖZ⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ"[::-1]
        output = ""
        for char in text:
            if char in all_text:
                output += all_up[all_text.index(char)]
            else:
                output += char
        await ctx.send(f"Flipped: {output[::-1]}\nUnflipped: {output}")
    
    @commands.guild_only()
    @commands.command()
    async def ascii(self, ctx, *, text):
        output = ""
        for char in text:
            output += str(ord(char))
        await ctx.send(output)
    
    @commands.guild_only()
    @commands.command()
    async def fromascii(self, ctx, *, text):
        output = ""
        full = text.split(" ")
        for char in full:
            output += chr(int(char))
        await ctx.send(output)
    
    @commands.guild_only()
    @commands.command()
    async def reverse(self, ctx, *, text):
        await ctx.send(text[::-1])

    @commands.guild_only()
    @commands.command(aliases=["rpw"])
    async def reverseperword(self, ctx, *, text):
        words = text.split(" ")
        output = ""
        for word in words:
            output += word[::-1] + " "
        await ctx.send(f"Flipped: {output[::-1]}\nUnflipped: {output}")

    @commands.guild_only()
    @commands.command()
    async def fliptext(self, ctx, *, text):
        output = ""
        all_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./~!@#$%^&*()_+{}|:\"<>?"
        all_output = "⸮><\":|}{+_()*&^%$#@!~/.ˎ';\][=-0୧8٢მटμƸςƖ`ZYXWVUTƧЯϘꟼOИM⅃ꓘႱIHӘꟻƎꓷƆꓭAzγxwvυɈƨɿpqonmlʞįiʜϱʇǝbɔdɒ"[::-1]
        for char in text:
            if char in all_text:
                output += all_output[all_text.index(char)]
            else:
                output += char
        await ctx.send(output)

    @commands.guild_only()
    @commands.command()
    async def lookup(self, ctx, *, query):
        try:
            query = int(query)
            try:
                is_guild = self.client.get_guild(query)
                await ctx.send(f"`{query}` is a guild with name {is_guild.name}")
            except:
                await ctx.send(f"`{query}` is not a guild")
                try:
                    is_channel = self.client.get_channel(query)
                    channel_guild = is_channel.guild
                    await ctx.send(f"`{query}` is a channel called `{is_channel.name}` belonging to guild `{channel_guild.name}` with id `{channel_guild.id}`.")
                except:
                    await ctx.send(f"`{query}` is not a channel.")
                    try:
                        is_user = self.client.get_user(query)
                        await ctx.send(f"`{query}` is a user called `{is_user.name}#{is_user.discriminator}`.")
                    except:
                        await ctx.send(f"`{query}` is not a user.")
                        try:
                            is_message = self.client.get_message(query)
                            await ctx.send(f"`{query}` is a message sent by `{is_message.author.name}#{is_message.author.discriminator}` with content:\n{is_message.content}")
                        except:
                            await ctx.send(f"Sorry, could not find `{query}`.")
        except:
            await ctx.send("Invalid Query!")

def setup(client):
    client.add_cog(Other(client))
