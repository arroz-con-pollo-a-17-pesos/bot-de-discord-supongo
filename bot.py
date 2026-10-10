import discord, random, os, requests
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def surprised(ctx):
    await ctx.send("O.O")

@bot.command()
async def bye(ctx):
    await ctx.send(f'Bye bye!')

@bot.command()
async def password(ctx):
    length = int(input("Ingrese la longitud de su contraseña "))
    password = gen_pass(length)
    await ctx.send(f"Tu contraseña es: {password}")

@bot.command()
async def emoticons(ctx):
    uhh = 1
    emoticons = random_emoticons(uhh)
    await ctx.send(emoticons)

@bot.command()
async def coin(ctx):
    coin = flip_coin()
    await ctx.send(coin)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f: 
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)



@bot.command()
async def guide(ctx):
    await ctx.send(f"!hello = El bot te saluda \n!heh = El bot se rie \n!surprised = El bot pone una cara sorprendida \n!bye = El bot se despide \n!password = Genera una contraseña aleatoria \n!emoticons = Muestra un emoticono aleatorio. \n!coin = El bot gira una moneda. \n!meme = inserta un meme aleatorio de 3 posibles. \n!duck = inserta una foto aleatoria de patitos. \n!dog = inserta una foto/video aleatoria de perritos")

bot.run("arf arf arf")
