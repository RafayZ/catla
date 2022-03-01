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

@commands.has_role('Blacklist')
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