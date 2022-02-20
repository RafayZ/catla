new cog who dis
class AniBlacklist(commands.Cog, name='Anigame Blacklist'):
    """Get blacklisted idiots"""

    def init(self, bot):
        self.bot = bot
    
    def cog_check(self, bot):
        pass #Whatever u wanna do

    @commands.Cog.listener()
    async def on_message(self, message):
        if msg.author.id != 571027211407196161:
            return 
        if not message.embeds:
            return
    
    @commands.is_owner()
    @commands.Command()
    async def addbl(self, ctx, id: int, *, reason:str):
        """Blacklist someone haha"""
        await self.bot.pool.execute("""INSERT INTO blacklist (uid, blacklisted, blreason) VALUES ($1, True, $2)
                ON CONFLICT (uid) DO UPDATE SET blacklisted = True, blreason = $2;
                """,
                id,
                reason,
            ) # this is the sql statement but pretty much requires learning
            # its basically saying to insert those info to columns, if the person alr exists then just blacklist
        await ctx.send("Blacklisted!")