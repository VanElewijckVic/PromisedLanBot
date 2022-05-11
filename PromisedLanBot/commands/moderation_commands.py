import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot

class moderation_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name = "ping")
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command(name = "RemoveTextChannel")
    async def RemoveTextChannel(self, ctx, arg):
        lines = arg.split()
        for x in lines:
            existing_channel = discord.utils.get(ctx.guild.text_channels, name = x)
            if existing_channel is None:
                await ctx.send(f"Error: `#{x.casefold()}` is not a text channel")
            else:
                await existing_channel.delete()
                await ctx.send(f"`#{x.casefold()}` has been deleted")

    @commands.command(name = "RemoveVoiceChannel")
    async def RemoveVoiceChannel(self, ctx, arg):
        lines = arg.split()
        for x in lines:
            existing_channel = discord.utils.get(ctx.guild.voice_channels, name = arg)
            if existing_channel is None:
                await ctx.send(f"Error: `:speaker: {x.casefold()} is not a voice channel")
            else:
                await existing_channel.delete()
                await ctx.send(f"`:speaker: {x.casefold()}` has been deleted")
    
    @commands.command(name = "purge")
    @commands.has_role("management")
    async def purge(self, ctx, arg: int):
        await ctx.channel.purge(limit = arg)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
    
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"You can't do that :x:")


def setup(client):
    client.add_cog(moderation_commands(client))