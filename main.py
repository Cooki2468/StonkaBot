import discord
from discord.ext import commands

file = open("bot_token.txt", "r")
token = file.readline()

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='')
wiadomosc = 'Gracze albiono to...\n' \
            ' Tacie ludzie którzy są ooo...\n' \
            ' Nie zawinę dziś do końca\n' \
            ' Bo spierdalam do ośrodka.\n' \
            ' Może zjebalem rymy\n' \
            ' A to i tak lepszy niż te ryny\n' \
            ' Lepsze rymy zawinę jutro\n' \
            ' Bo dziś zwijany będę niczym łóżko'


@bot.command(name="jestem")
async def jestem(context, arg):
    if arg == "fajny?":
        await context.reply('albo inaczej')


@bot.command(name="albion")
async def albion(context):
    await context.reply(wiadomosc)


@bot.command(name="wew")
async def albion(context):
    await context.reply('rasa')


bot.run(token)
