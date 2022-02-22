import discord
from discord.ext import commands

class Anicomp(commands.Cog, name = "Anigame Comps"):
    """Comps for Anigame bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dcomp(ctx, name):
        await ctx.send("Please note that high level rare comps can also be used on SR,UR raids.")
        comp_table = '''CREATE TABLE comps(
            name TEXT,
            comp TEXT
        );'''
        await self.bot.pool.execute('''INSERT INTO comps (name, comp)
        VALUES
          (Ranpo, For Sr,Ur max & rare 1000-2200: Arde, Ikumi, Ikumi (all Sr) or Senku, Jiraiya/Loke, Dio/Gasai (all Sr)),
          (Nico, For Sr,Ur max & rare 1000-2200: Izumo, Mukuro, Iris (2 UR))''')
        for names in comps:
            if name == names.title():
                return await ctx.send(comp(name))
        await ctx.send("Please enter a valid name or DM my master if the card of your choice is not present.")

def setup(bot):
    bot.add_cog(Anicomp(bot))
