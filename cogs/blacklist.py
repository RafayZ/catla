import discord
from discord.ext import commands
import re
class AniBlacklist(commands.Cog, name='Anigame Blacklist'):
    """Get blacklisted idiots"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 571027211407196161:
            return 
        if not message.embeds:
            return
        embed = message.embeds[0]
        if embed.footer.text.endswith("Type .rd start whenever the party is ready!"):
            users = re.findall(r'\(([0-9]{15,19})\)', str(embed.to_dict())) #get all the ids in lobby
            for user in users: #check them individually
                blcheck = await self.bot.pool.fetchrow("""SELECT * FROM blacklist WHERE "uid"=$1 and blacklisted;""", int(user))
                if blcheck:
                    message.channel.send(f'{user} is blacklisted!')
    
    @commands.is_owner()
    @commands.command()
    async def addbl(self, ctx, id: int, *, reason:str):
        """Blacklist someone haha"""
        await self.bot.pool.execute("""INSERT INTO blacklist (uid, blacklisted, reason) VALUES ($1, True, $2)
                ON CONFLICT (uid) DO UPDATE SET blacklisted = True, reason = $2;
                """,
                id,
                reason,
            ) # this is the sql statement but pretty much requires learning
            # its basically saying to insert those info to columns, if the person alr exists then just blacklist
        await ctx.send("Blacklisted!")

def setup(bot):
    bot.add_cog(AniBlacklist(bot)) 