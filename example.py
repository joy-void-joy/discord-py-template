from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot, authorized_ids=[], authorized_guilds=[]):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello world")

def setup(bot):
    bot.add_cog(Example(bot))
