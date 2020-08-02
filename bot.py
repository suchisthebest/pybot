import discord
from discord.ext import commands

client = commands.Bot(command_prefix='bot.')
message = discord.message

version = '1.0'


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('i was just born'))
    print('Bot is ready ' + version)


client.run('*bot token here*')
