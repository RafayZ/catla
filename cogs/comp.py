import discord
from discord.ext import commands

class Anicomp(commands.Cog, name = "Anigame Comps"):
    """Comps for Anigame bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dcomp(self, ctx, name):
        comp_table = '''CREATE TABLE comps(
            names TEXT,
            comp TEXT
        );'''
        await self.bot.pool.execute('''INSERT INTO comps (names, comp)
        VALUES
          ('ranpo', 'For Sr/Ur Max & rare 1000-2200: Arde Ikumi Ikumi (all SR) Or Senku Jiraiya/Loke Dio/Gasai (all SR)'),
          ('nico', 'For Sr/Ur Max & rare 1000-2200: Izumo Mukuro Iris (2 UR)'),
          ('iz', 'For Sr/Ur max & rare 1000-2200: Ranpo Motoyasu Dio (1 UR)'),
          ('machi', 'For Sr/Ur max: Doppo Koshi Shion (all SR) Or Josuke Doppo Shion (all SR). For rare 1800-2200: Doppo Koshi Shion (1 UR)'),
          ('sora', 'For Sr/Ur max & rare 1000-2200: Kenma Shoto Fuyumi (all Sr)'),
          ('hinawa', 'For Sr/Ur max & rare 1000-1800: Shoto Gowther Fuyumi (all Sr). For rare 1800-2100: Jonathan Iz Elma (1 Ur)'),
          ('izumo', 'For Sr/Ur max & rare 1000-1600: Rize Doppo/Iz Nezuko. For rare 1600+: Nico Shoto Gasai (1 Ur min)'),
          ('shoto', 'For Sr/Ur max & rare 1500-2200: Nishinoya Iz/Yukina Killua/Kenpachi (Ur Para is a must 1-2 Ur). For rare 1000-1500: Ranpo Motoyasu Dio (1-2 Ur)'),
          ('star', 'For Sr/Ur max & rare 1000-1600: Doppo Koshi Shion (1 Ur for Sr max. 2 Ur for above). For rare 1600+ Doppo Koshi Gin (2-3 Ur)'),
          ('doppo', 'For Sr/Ur max & rare 1000-2100: Sora/Kanade Hinawa Baji (all Sr). For rare 2200+: Sora/Kanade Hinawa Baji (1-2 Ur)'),
          ('iris', 'For Sr/Ur max & rare 1000-1500: Kenma/Hydra Shoto Gasai/Dio/Wolf (1 Ur). For rare 1600+: Kenma/Hydra Shoto Gasai/Dio/Wolf (2 Ur)'),
          ('loke', 'For Sr/Ur max & rare 1000-1800: Doppo Koshi Shion Or Josuke Doppo Shion (all Sr). For rare 1800+: Doppo Koshi Shion (1-2 Ur)'),
          ('shion', 'For Sr/Ur max & rare 1000-1600: Sora/Kanade Hinawa Baji (all Sr). For rare 1600+: Sora/Kanade Hinawa Baji (1-2 Ur)'),
          ('yukina', 'For Sr/Ur max & rare 1000-1700: Ranpo Motoyasu Dio (1 UR). For rare 1700+: Ranpo Motoyasu Dio (1-2 UR)')
          ('edward', 'For Sr/Ur max & rare 1000-2000: Josuke Doppo Star (all Sr). For rare 2200+: Nico Shoto Tsukasa (1-2 Ur)'),
          ('baji', 'For Sr/Ur max & rare 1000-2000: Gowther Kenma/Padoru Fuyumi/Saika. For rare 2000+: Gowther Padoru/Kenma Fuyumi/Saika (1-2 Ur)'),
          ('anna', 'For Sr/Ur max & rare 1000-1600: Ririka Artoria Byakuya or Ranpo/Gowther Motoyasu Dio/Wolf/Byakuya (1 Ur recommended on Gowther comp). For rare 1600+:Ririka Artoria Kirari (2-3 Ur)'),
          ('gasai', 'For Sr/Ur max & rare 1000-2200: Izumo Nico Gasai (1-2 Ur). For rare 1550 and below: Izumi/Wiz/Mayuri Motoyasu Gasai/Dio/Wolf(0-1 Ur)'),
          ('yami', 'For Sr/Ur max and rare 1500+: Izumo Naraku/Maria Ban (1-2 Ur). For rare 1500 and below: Rize Wiz/Mayuri/Izumi Iris (0-1 Ur)'),
          ('shalltear', 'For Sr/Ur max & rare 1000-1650: Prince Nico/Hydra Gasai/Zombieman (1-2 Ur). For rare 1650+: Yami Nico/Hydra Iris (1-3 Ur)'),
          ('senku', 'For Sr/Ur max & rare 1000-1550: Violet/Riko Jiraiya/Loke Gasai/Wolf (0-1 Ur). For rare 1600+: Violet/Riko Jiraiya/Loke Gasai/Wolf (2-3 Ur)'),
          ('ritsu', 'For Sr/Ur max & rare 1000-2200: Josuke Ikumi Ikumi (all Sr). For Sr max & rare 1550: Machi Loke Ikumi (all Sr)'),
          ('motoyasu', 'For Sr/Ur max & rare 1000-1900: Ranpo Loke Machi (0-1 Ur). For rare 2000+: Josuke Ikumi Ikumi (0-1 Ur)'),
          ('elma', 'For Sr/Ur max & rare 1000-1700: Motoyasu Ranpo Dio (0-1 Ur). For rare 1750+: Ranpo Motoyasu Dio (1-2 Ur)'),
          ('gowther', 'For Sr/Ur max & rare 1000-2200: Kenma Shoto Dio (all Sr) Or Nishinoya Yukina/Iz Ritsu (all Sr). For rare 2200+: Kenma Shoto Dio (0-1 Ur)'),
          ('ikumi', 'For Sr max & rare 1000-1300: Doppo Koshi Shion (all Sr). For Ur max & rare 1400+: Doppo Koshi Shion (1-2 Ur). For high crazy pl: Elaine Riko/Violet Iris/Ikumi(2-3 Ur)'),
          ('kurosaki', 'For Sr/Ur max & rare 1500+: Izumo Wiz/Mayuri/Izumi Ban (1-2 Ur). For rare 1500 and below: Izumo Wiz/Mayuri/Izumi Ban (0-1 Ur)'),
          ('escanor', 'For Sr/Ur max & rare 1000-1600: Gowther Padoru/Kenma/Wiz/Izumi Fuyumi/Saika (all Sr). For rare 1650+: Gowther Padoru/Kenma/Wiz/Izumi Fuyumi/Saika (1-2 Ur). For crazy high pl: Maki Gowther Fuyumi (0-2 Ur)'),
          ('dio', 'For Sr/Ur max & rare 1000-1700: Senku Jiraiya/Loke Dio (all Sr). For rare 1750+: Senku Jiraiya/Loke Dio (1-2 Ur). For crazy high pl: Arde Ikumi Ikumi Or Ranpo Hydra Iris/Ikumi (3 Ur)'),
          ('byakuya', 'For Sr/Ur max & rare 1000-1800: Kenma Shoto Dio/Wolf/Byakuya (all Sr). For rare 1800+: Kenma Shoto Dio/Wolf/Byakuya (1-2 Ur)')
          ('artoria', 'For Sr/Ur max & rare 1000-1550: Sayaka Kurapika Kirari/Iris(3 Ur) For rare 1550+: Ririka Kurapika Kirari/Iris(3 Ur)');''')
        namess = await self.bot.pool.fetchrow(""" SELECT * FROM comps WHERE names = $1;""", name )
        if namess:
            await ctx.send("Please note that high level rare comps can also be used on SR,UR raids.")
            return await ctx.send(f'{namess["comp"]}')
        else:
            await ctx.send("Please enter a valid name or DM my master if the card of your choice is not present.")

def setup(bot):
    bot.add_cog(Anicomp(bot))
