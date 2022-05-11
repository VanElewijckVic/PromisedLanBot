import os

import discord
from discord.ext import commands

TOKEN = 'OTAwMzI4NDAzNTY2MjAyOTEw.YW_uKg.0Wr1onGsQiHeslRPl4G_Fo9gSp8'
GUILD = 'apserver'

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '$', intents = intents)
guild = client.get_guild(GUILD)

cog_files = ["commands.game_commands", "commands.moderation_commands"]


for cog_file in cog_files:
        client.load_extension(cog_file)
        print(f"{cog_file} has been loaded")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f"{client.user} is connect to the following server: \n"
          f"{guild.name} (id: {guild.id}) \n"
          f"Bot has started!!")


client.run(TOKEN)