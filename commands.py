import discord

from discord.ext import commands

client = commands.Bot(command_prefix="%")

version = '1.0'
invite = 'https://discordapp.com/oauth2/authorize?client_id=736742593505001593&scope=bot&permissions=2146958847'
coderbot = 'https://discord.gg/rtjbdHu'


@client.event
async def on_ready():
    print('Bot is ready and it is running version ' + version)


@client.command()
async def hello(ctx, arg1, arg2):
    await ctx.send("hello " + arg1 + ", " + arg2)


@client.command()
async def yo(ctx, arg1, arg2):
    await ctx.send("well hello there " + arg1 + ", " + arg2 + "!")


@client.command()
async def invite(ctx):
    await ctx.send('to invite me to your server use this link: ' + invite)


@client.command()
async def discord(ctx):
    await ctx.send('here is our coderbot server: ' + coderbot)


@client.command()
async def helpcom(ctx):
    await ctx.send('here are all the commands (still under development): ```%helpcom```, ```%lol```, ```%invite```, '
                   '```%discord```')


client.run('your bot token here')
