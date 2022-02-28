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
                    username = await self.bot.fetch_user(user)
                    await message.channel.send(f'⚠️ {username.name}#{username.discriminator} is blacklisted! Reason: {blcheck["reason"]} ⚠️')
    
    #@commands.has_role('Blacklist')
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
        channel = self.bot.get_channel(944965304973402232)
        username = await self.bot.fetch_user(id)
        await channel.send(f'{username} was blacklisted by {ctx.author.name}')

    @commands.command()
    async def delbl(self, ctx, user_id: int):
        """Remove from blacklist :p"""
        await self.bot.pool.execute('''delete from blacklist where uid = 1$;''', user_id
    )
        username = await self.bot.fetch_user(user_id)
        await ctx.send(f"Removed {username} from Blacklist!")

def setup(bot):
    bot.add_cog(AniBlacklist(bot)) 