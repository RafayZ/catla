import discord, asyncio, aiohttp
from discord.ext import commands
import random, config, db, os, asyncpg

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

class Catlas(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        allowed_mentions = discord.AllowedMentions.none()
        allowed_mentions.users = True
        super().__init__(command_prefix='&',
        max_messages=1000,
        intents=intents,
        allowed_mentions=allowed_mentions)
        
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")

    def run(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(db.Table.create_pool(config.postgresql))
        self.session = aiohttp.ClientSession()
        self.config = config
        super().run(*args, **kwargs)

    async def close(self):
        await self.session.close()
        await super().close()

bot = Catlas()
os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'

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
      await message.channel.send("<@&945698593971535962>, server drop guys!", allowed_mentions=discord.AllowedMentions.all())

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


#@bot.command()
#async def dcomp(ctx, name):
    """Command to check different comps for raids in the Anigame bot"""
    await ctx.send('Please note that high level rare comps can also be used backwards.')
    comps = {
        'Ranpo' : ["For Sr,Ur max & rare 1000-2200: Arde, Ikumi, Ikumi (all Sr) or Senku, Jiraiya/Loke, Dio/Gasai (all Sr)"],
        'Nico' : ["For Sr,Ur max & rare 1000-2200: Izumo, Mukuro, Iris (2 UR)"],
        'Iz' : ["For Sr,Ur max & rare 1000-2200: Ranpo, Motoyasu, Dio (1 UR)"],
        'Machi' : ["For Sr,Ur max: Doppo, Koshi, Shion (all SR) or Josuke, Doppo, Shion (all Sr)", "For rare 1800-2200: Doppo, Koshi, Shion (1 UR)"],
        'Sora' : ["For Sr,Ur max & rare 1000-2200: Kenma, Shoto, Fuyumi (all Sr)"],
        'Hinawa' : ["For Sr,Ur max & rare 1000-1800: Shoto, Gowther, Fuyumi (all Sr)", "For rare 1800-2100: Jonathan, Iz, Elma (1 Ur)"],
        'Izumo' : ["For Sr,Ur max & rare 1000-1600: Rize, Doppo/Iz, Nezuko", "For rare 1600+: Nico, Shoto, Gasai (1 Ur min)"],
        'Shoto' : ["For Sr,Ur max & rare 1500-2200: Nishinoya, Iz/Yukina, Killua/Kenpachi (Ur Para is a must, 1-2 Ur)", "For rare 1000-1500: Ranpo, Motoyasu, Dio (1-2 Ur)"],
        'Star' : ["For Sr,Ur max & rare 1000-1600: Doppo, Koshi, Shion (1 Ur for Sr max, 2 Ur for above)", "For rare 1600+ Doppo, Koshi, Gin (2-3 Ur)"],
        'Doppo' : ["For Sr,Ur max & rare 1000-2100: Sora/Kanade, Hinawa, Baji (all Sr)", "For rare 2200+: Sora/Kanade, Hinawa, Baji (1-2 Ur)"],
        'Iris' : ["For Sr,Ur max & rare 1000-1500: Kenma/Hydra, Shoto, Gasai/Dio/Wolf (1 Ur)", "rare 1600+: Kenma/Hydra, Shoto, Gasai/Dio/Wolf (2 Ur)"],
        'Loke' : ["For Sr,Ur max & rare 1000-1800: Doppo, Koshi, Shion Or Josuke, Doppo, Shion (all Sr)", "rare 1800+: Doppo, Koshi, Shion (1-2 Ur)"],
        'Shion' : ["For Sr,Ur max & rare 1000-1600: Sora/Kanade, Hinawa, Baji (all Sr)", "For rare 1600+: Sora/Kanade, Hinawa, Baji (1-2 Ur)"],
        'Yukina' : ["For Sr,Ur max & rare 1000-1700: Ranpo, Motoyasu, Dio (1 UR)", "For rare 1700+: Ranpo, Motoyasu, Dio (1-2 UR)"],
        'Edward' : ["For Sr,Ur max & rare 1000-2000: Josuke, Doppo, Star (all Sr)", "For rare 2200+: Nico, Shoto, Tsukasa (1-2 Ur)"],
        'Black Star' : ["For Sr,Ur max & rare 1000-1600: Doppo, Koshi, Shion (1 Ur for Sr max, 2 Ur for above)", "For rare 1600+ Doppo, Koshi, Gin (2-3 Ur)"],
        'Bstar' : ["For Sr,Ur max & rare 1000-1600: Doppo, Koshi, Shion (1 Ur for Sr max, 2 Ur for above)", "For rare 1600+ Doppo, Koshi, Gin (2-3 Ur)"],
        'Baji' : ["For Sr,Ur max & rare 1000-2000: Gowther, Kenma/Padoru, Fuyumi/Saika", "For rare 2000+: Gowther, Padoru/Kenma, Fuyumi/Saika (1-2 Ur)"],
        'Anna' : ["For Sr,Ur max & rare 1000-1600: Ririka, Artoria, Byakuya or Ranpo/Gowther, Motoyasu, Dio/Wolf/Byakuya (1 Ur recommended on Gowther comp)", "For rare 1600+:Ririka, Artoria, Kirari (2-3 Ur)"],
        'Gasai' : ["For Sr,Ur max & rare 1000-2200: Izumo, Nico, Gasai (1-2 Ur)", "For rare 1550 and below: Izumo, Motoyasu, Gasai/Dio/Wolf(0-1 Ur)"],
        'Yami' : ["For Sr,Ur max and rare 1500+: Izumo, Naraku/Maria, Ban (1-2 Ur)", "For rare 1500 and below: Rize, Wiz/Mayuri/Izumi, Iris (0-1 Ur)"],
        'Shalltear' : ["For Sr,Ur max & rare 1000-1650: Prince, Nico/Hydra, Gasai/Zombieman (1-2 Ur)", "For rare 1650+: Yami, Nico/Hydra, Iris (1-3 Ur)"],
        'Senku' : ["For Sr,Ur max & rare 1000-1550: Violet/Riko, Jiraiya/Loke, Gasai/Wolf (0-1 Ur)", "For rare 1600+: Violet/Riko, Jiraiya/Loke, Gasai/Wolf (2-3 Ur)"],
        'Ritsu' : ["For Sr,Ur max & rare 1000-2200: Josuke, Ikumi, Ikumi (all Sr)", "For Sr max, rare 1550: Machi, Loke, Ikumi (all Sr)"],
        'Motoyasu' : ["For Sr,Ur max & rare 1000-1900: Ranpo, Loke, Machi (0-1 Ur)", "For rare 2000+: Josuke, Ikumi, Ikumi (0-1 Ur"],
        'Elma' : ["For Sr,Ur max & rare 1000-1700: Motoyasu, Ranpo, Dio (0-1 Ur)", "For rare 1750+: Ranpo, Motoyasu, Dio (1-2 Ur)"],
        'Gowther' : ["For Sr,Ur max & rare 1000-2200: Kenma, Shoto, Dio (all Sr) Or Nishinoya, Yukina/Iz, Ritsu (all Sr)", "For rare 2200+: Kenma, Shoto, Dio (0-1 Ur)"],
        'Ikumi' : ["For Sr max & rare 1000-1300: Doppo, Koshi, Shion (all Sr)", "For Ur max & rare 1400+: Doppo, Koshi, Shion (1-2 Ur)", "For high crazy pl: Elaine, Riko/Violet, Iris/Ikumi"],
        'Mito' : ["For Sr max & rare 1000-1300: Doppo, Koshi, Shion (all Sr)", "For Ur max & rare 1400+: Doppo, Koshi, Shion (1-2 Ur)", "For high crazy pl: Elaine, Riko/Violet, Iris/Ikumi"],
        'Kurosaki' : ["For Sr,Ur max & rare 1500+: Izumo, Wiz/Mayuri/Izumi, Ban (1-2 Ur)", "For rare 1500 and below: Izumo, Wiz/Mayuri/Izumi, Ban (0-1 Ur)"],
        'Escanor' : ["For Sr,Ur max & rare 1000-1600: Gowther, Padoru/Kenma/Wiz/Izumi, Fuyumi/Saika (all Sr)", "For rare 1650+: Gowther, Padoru/Kenma/Wiz/Izumi, Fuyumi/Saika (1-2 Ur)", "For crazy high pl: Maki, Gowther, Fuyumi (0-2 Ur)"],
        'Dio' : ["For Sr,Ur max & rare 1000-1700: Senku, Jiraiya/Loke, Dio (all Sr)", "For rare 1750+: Senku, Jiraiya/Loke, Dio (1-2 Ur)", "For crazy high pl: Arde, Ikumi, Ikumi Or Ranpo, Hydra, Iris/Ikumi (3 Ur)"],
        'Byakuya' : ["For Sr,Ur max & rare 1000-1800: Kenma, Shoto, Dio/Wolf/Byakuya (all Sr)", "For rare 1800+: Kenma, Shoto, Dio/Wolf/Byakuya (1-2 Ur)"]
        }
    for key in comps:
        if key == name.title():
            return await ctx.send(comps[key])
    await ctx.send('Please enter a valid name or DM my master if the card of your choice is not present.')

@bot.command()
async def blacklist(ctx):
    """A command to blacklist user's from using this bot."""
    blacklist = []
    await ctx.message.delete()
    if ctx.author.id in blacklist:
        await ctx.send("You are blacklisted")
    else:
        return

bot.load_extension("jishaku")


bot.run(config.token)