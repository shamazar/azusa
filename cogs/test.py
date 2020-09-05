from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx, *args):
        await ctx.send(self.bot.config['bot']['test'])

def setup(bot):
    bot.add_cog(Test(bot))
