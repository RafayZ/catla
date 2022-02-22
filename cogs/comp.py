import discord
from discord.ext import commands

class Anicomp(commands.Cog, name = "Anigame Comps"):
    """Comps for Anigame bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dcomp(self, ctx, name):
        await ctx.send("Please note that high level rare comps can also be used on SR,UR raids.")
        comp_table = '''CREATE TABLE comps(
            names TEXT,
            comp TEXT
        );'''
        await self.bot.pool.execute('''INSERT INTO comps (names, comp)
        VALUES
          ('Ranpo', 'For Sr/Ur Max & rare 1000-2200: Arde Ikumi Ikumi (all SR) or Senku Jiraiya/Loke Dio/Gasai (all SR)'),
          ('Nico', 'For Sr/Ur Max & rare 1000-2200: Izumo Mukuro Iris (2 UR)');''')
        namess = await self.bot.pool.fetchrow(""" SELECT * FROM comps WHERE names = name;""" )
        return await ctx.send(namess)
        await ctx.send("Please enter a valid name or DM my master if the card of your choice is not present.")

def setup(bot):
    bot.add_cog(Anicomp(bot))
