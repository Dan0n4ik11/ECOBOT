import discord
from discord.ext import commands
import requests
import random
import emoji
import emojis

bot = commands.Bot(command_prefix='+', intents=discord.Intents().all())


@bot.command('rmem')
async def randommem(ctx):
    a = ['project/mem1.jpg', 'project/mem2.jpg', 'project/mem3.jpg']
    b = random.randint(0, 2)
    with open(a[b], 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command('rduck')
async def duck(ctx):
    def get_duck_image_url():
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('rmot')
async def cute(ctx):
    a = ['Ты лучший :red_heart:',
         'У тебя всё получится :thumbsup:', 'Удачи тебе :smile:']
    b = random.randint(0, 2)
    await ctx.reply(a[b])
    c = ['project/cat1.jpg', 'project/cat2.jpg', 'project/cat3.jpg',
         'project/cat4.jpg', 'project/cat5.jpg',]
    d = random.randint(0, 4)
    with open(c[d], 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command('yt')
async def yt(ctx):
    await ctx.reply('''Ссылка на канал гринпис https://www.youtube.com/@greenpeace
Ссылка на канал WWF https://www.youtube.com/@WWFunitedkingdom''')


@bot.command('h')
async def help(ctx):
    await ctx.reply('''Список в данный момент существующих команд:
yt
plastic
metal
dirt
wood
clay
stone
glass
concrete''')

# alexander part


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


bot.run('TOKEN')

