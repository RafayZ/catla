import discord
from discord.ext import commands

class Anicomp(commands.Cog, name = "Anigame Comps"):
    """Comps for Anigame bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dcomp(self, ctx, name):
        namess = await self.bot.pool.fetchrow(""" SELECT * FROM comps WHERE names = $1;""", name )
        if namess:
            await ctx.send("Please note that high level rare comps can also be used on SR,UR raids.")
            return await ctx.send(f'{namess["comp"]}')
        else:
            await ctx.send("Please enter a valid name or DM my master if the card of your choice is not present.")

def setup(bot):
    bot.add_cog(Anicomp(bot))
