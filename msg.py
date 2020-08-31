import discord
from discord.ext import commands
from matplotlib.figure import Figure
import json, matplotlib.pyplot as plt, os, matplotlib as mpl

f = open("messages.json")
messages = json.load(f)
msg_count = 0

class Msg(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            try:
                messages[str(message.author.id)] += 1
            except:
                messages[str(message.author.id)] = 1
            with open("messages.json", "w") as f:
                json.dump(messages, f)
        if message.content == "<@748739858091999363>":
            channel = message.channel
            await channel.send(f"Hi! My prefix for this guild is {get_prefix(self.client, message)}")
        # await self.client.process_commands(message)
    

    @commands.guild_only()
    @commands.command(aliases=["track"])
    async def trackmessages(self, ctx):
        await ctx.send(f"{ctx.author} sent {messages[str(ctx.author.id)]} messages.")

    @commands.guild_only()
    @commands.command(aliases=["msgbar"])
    async def messagebar(self, ctx, *, color="blue white black"):
        top = []
        leaderboard = []
        sorted_msg = {k: v for k, v in sorted(messages.items(), key=lambda item: item[1])}
        c = color.split(" ")
        for key in sorted_msg:
            top.append(self.client.get_user(int(key)).name)
            leaderboard.append(sorted_msg[key])
        for i in range(len(top)):
            if len(top[i]) > 16:
                top[i] = top[i][:13] + "..."
        try:
            leaderboard = leaderboard[:9]
            top = top[:9]
        except:
            pass
        mpl.rc("font", size=40)
        fig = plt.figure(figsize=(42, 21))
        ax = fig.add_subplot(1, 1, 1)
        ax.barh(top, leaderboard, color=c[0])
        try:
            ax.set_facecolor(c[1])
            fig.set_facecolor(c[1])
            plt.title("Bar Graph Showing Message Leaderboard", color=c[2])
            plt.ylabel("Messages sent", color=c[2])
            plt.xlabel("Top Users", color=c[2])
            try:
                ax.tick_params(axis="x", colors=c[2])
                ax.tick_params(axis="y", colors=c[2])
            except:
                if c[1] == "black" or c[1] == "#000" or c[1] == "#000000":
                    ax.tick_params(axis="x", colors="#fff")
                    ax.tick_params(axis="y", colors="#fff")
        except:
            pass
        plt.savefig("fig.png")
        f = discord.File("fig.png")
        await ctx.send(file=f)
        os.remove("fig.png")

    @commands.guild_only()
    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx):
        top = []
        leaderboard = []
        sorted_msg = {k: v for k, v in sorted(messages.items(), key=lambda item: item[1], reverse=True)}
        for key in sorted_msg:
            top.append(self.client.get_user(int(key)).name)
            leaderboard.append(sorted_msg[key])
        try:
            leaderboard = leaderboard[:9]
            top = top[:9]
        except:
            pass
        e = discord.Embed(title="Leaderboard", color=0x0000ff)
        for i in range(len(leaderboard)):
            e.add_field(name=top[i], value=leaderboard[i])
        await ctx.send(embed=e)

def get_prefix(client, message):
    with open("prefixes.json") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

def setup(client):
    client.add_cog(Msg(client))