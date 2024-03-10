import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+', intents=discord.Intents().all())


@bot.event
async def on_ready(ctx):
    print(f'logged {bot.user}')
    await ctx.send(f'ПРИВЕТ {bot.user}!')


@bot.command('plastic')
async def plastic(ctx):
    await ctx.send(f'25%')


@bot.command('metal')
async def metal(ctx):
    await ctx.send(f'25%')


@bot.command('dirt')
async def dirt(ctx):
    await ctx.send(f'100%')


@bot.command('wood')
async def wood(ctx):
    await ctx.send(f'100%')


@bot.command('clay')
async def clay(ctx):
    await ctx.send(f'100%')


@bot.command('stone')
async def stone(ctx):
    await ctx.send(f'100%')


@bot.command('glass')
async def glass(ctx):
    await ctx.send(f'90%')


@bot.command('concrete')
async def concrete(ctx):
    await ctx.send(f'50%')


@bot.command('ecohelp')
async def help(ctx):
    await ctx.reply('''+yt - ссылки на ютуб каналы эко-организаций''')


@bot.command('yt')
async def yt(ctx):
    print('''Ссылка на канал гринпис https://www.youtube.com/@greenpeace
          Ссылка на канал WWF https://www.youtube.com/@WWFunitedkingdom''')


bot.run('MTIxNjE1OTkzODg0MjIwMjE0Mw.GqK48H.6GN9d6r31F7hAOuEuKruyLKNmzgdLz3T_fejX8')
