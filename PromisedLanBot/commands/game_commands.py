import os

import discord
from discord.channel import CategoryChannel

from discord.client import Client
from discord.ext import commands
from discord.ext.commands.core import group

path = "json/Games.txt"

colors =  {"green" : 0x00ff00, "red" : 0xff0000, "blue" : 0x0000ff}

class game_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.server = "apserver"

    @commands.command(name = "AddGame")
    async def AddGame(self, ctx, arg):
        games = arg.split()
        channelCategory = discord.utils.get(ctx.guild.categories, name = "Games")
        category = ''

        if channelCategory is None:
            category = await ctx.guild.create_category_channel("Games")
        else:
            category = channelCategory
        
        for game in games:
            if os.path.isfile(path):
                file = open(path, 'r')
                for line in file:
                    if line.split('\n')[0].casefold() == game.casefold():
                        await ctx.send(f"Game `{game.casefold()}` is already in the list")
                        return
                        
            if os.path.isfile(path):
                file = open(path, 'a')
                file.write(game + "\n")

                embed = discord.Embed(title = "Added game(s)", description = f"Game `{game}` has been added to the list of games", color = colors["green"])
                embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)

                await ctx.guild.create_text_channel(game, category = category)
                await ctx.send(embed = embed)

            elif not os.path.isfile(path):
                file = open(path, 'a')
                file.write(game + "\n")

                embed = discord.Embed(title = "Added game(s)", description = f"Game `{game}` has been added to the list of games", color = colors["green"])
                embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)

                await ctx.guild.create_text_channel(game, category = category)
                await ctx.send(f"Game `{game.casefold()}` has been added to the list of games")
                file.close()
        

    @commands.command(name = "RemoveGame")
    async def RemoveGame(self, ctx, arg):
        existing_channel = discord.utils.get(ctx.guild.text_channels, name = arg)
       
        if os.path.isfile(path):
            file = open(path, 'r')
            lines = file.readlines()
            file.close()

            file = open(path, 'w')
            for line in lines: # Removing from file
                if line.strip('\n').casefold() != arg.casefold():
                    file.write(line)

            # Removing channel
            if existing_channel is None:
                    await ctx.send(f"Error: `{arg.casefold()}` got deleted from list but channel does not exist")
            else:
                await existing_channel.delete()
                await ctx.send(f"Channel `{arg.casefold()}` has been deleted!")

    @commands.command(name = "ListGames")
    async def ListGames(self, ctx):
        gamesList = ""
        
        # Opens file and puts al games in a STRING
        if os.path.isfile(path):
            file = open(path, 'r')
            lines = file.readlines()
            file.close()

            for line in lines:
                gamesList = gamesList + line

        # The embed to show the list in discord
        embed = discord.Embed(title = "List of all games", description = gamesList, color = discord.Color.blue())
        embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)

        # Bot send message
        await ctx.send(embed = embed)
                    
    @commands.command(name = "random")
    async def randomChampion(self, ctx):
            await ctx.send(f"y or n")
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n"]
            
            msg = await commands.client.wait_for("message", check = check)
            if msg.content.lower() == "y":
                await ctx.send("You said yes!")
            else:
                await ctx.send("You said no!")


def setup(client):
    client.add_cog(game_commands(client))