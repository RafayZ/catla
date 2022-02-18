import discord
from discord.ext import commands
import random, config

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.listen('on_message')
async def Karuta(message):
    if message.guild.id != 921640800255901737:
        return
    if message.content == "I'm dropping 3 cards since this server is currently active!":
      await message.channel.send("<@&943782735179309096>, server drop guys!")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool!')


@bot.command()
async def dcomp(ctx, name=str):
    await ctx.send('Please note that high level rare comps can also be used backwards.')
    comps = {
        'Ranpo' : ["For Sr,Ur max & rare 1000-2200: Arde, Ikumi, Ikumi (all Sr) or Senku, Jiraiya/Loke, Dio/Gasai (all Sr)"],
        'Nico' : ["For Sr,Ur max & rare 1000-2200: Izumo, Mukuro, Iris (2 UR)"],
        'Iz' : ["For Sr,Ur max & rare 1000-2200: Ranpo, Motoyasu, Dio (1 UR)"],
        'Machi' : ["For Sr,Ur max: Doppo, Koshi, Shion (all SR) or Josuke, Doppo, Shion (all Sr)", "For rare 1800-2200: Doppo, Koshi, Shion (1 UR)"],
        'Sora' : ["For Sr,Ur max & rare 1000-2200: Kenma, Shoto, Fuyumi (all Sr"],
        'Hinawa' : ["For Sr,Ur max & rare 1000-1800: Shoto, Gowther, Fuyumi (all Sr)", "For rare 1800-2100: Jonathan, Iz, Elma (1 Ur)"],
        'Izumo' : ["For Sr,Ur max & rare 1000-1600: Rize, Doppo/Iz, Nezuko", "For rare 1600+: Nico, Shoto, Gasai (1 Ur min)"],
        'Shoto' : ["For Sr,Ur max & rare 1500-2200: Nishinoya, Iz/Yukina, Killua/Kenpachi (Ur Para is a must, 1-2 Ur)", "For rare 1000-1500: Ranpo, Motoyasu, Dio (1-2 Ur)"],
        'Star' : ["For Sr,Ur max & rare 1000-1600: Doppo, Koshi, Shion (1 Ur for Sr max, 2 Ur for above)", "For rare 1600+ Doppo, Koshi, Gin (2-3 Ur)"]
        }
    for key in comps:
        if key == name.title():
            await ctx.send(comps[key])
        else:
            await ctx.send('Please enter a valid name or DM my master if the card of your choice is not present.')


bot.load_extension("jishaku")


bot.run(config.token)