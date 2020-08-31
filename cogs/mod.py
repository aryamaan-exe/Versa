import discord
from discord.ext import commands
import asyncio

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member} has been banned from this planet 😉")
    
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"{member} has been kicked from this planet 😉")
    
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                ctx.guild.unban(user)
                await ctx.send("Fine, they can come back.")
                await asyncio.sleep(2)
                await ctx.send(f"Welcome back, {user}!")
    
    # @commands.guild_only()
    # @commands.has_permissions(ban_members=True)
    # @commands.command()
    # async def tempban(self, ctx, member: discord.Member, *, dar):
    #     duration = dar.split(" ")[0]
    #     try:
    #         reason = dar.split(" ")[1]
    #     except:
    #         reason = None
    #     time = duration[:-1]
    #     if duration.endswith("m"):
    #         time *= 60
    #     elif duration.endswith("h"):
    #         time *= 3600
    #     elif duration.endswith("d"):
    #         time *= 86400
    #     time = int(time)
    #     mname = member.name
    #     discrim = member.discriminator
    #     await ctx.guild.ban(member, reason=reason)
    #     await ctx.send(f"{member} has been exiled for `{duration}`. They'll come back, dw.")
    #     await asyncio.sleep(time)
    #     await ctx.guild.unban(f"{mname}#{discrim}")
    #     await ctx.send(f"Okay. It has been `{duration}` and I just unbanned {member}.")


def setup(client):
    client.add_cog(Mod(client))
