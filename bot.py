import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

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
async def guide(ctx):
    await ctx.send(f"$hello = El bot te saluda \n$heh = El bot se rie \n$surprised = El bot pone una cara sorprendida \n$bye = El bot se despide \n$password = Genera una contraseña aleatoria \n$emoticons = Muestra un emoticono aleatorio. \n$coin = El bot gira una moneda")

bot.run("meow")
