from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, *args):
        if self.bot.is_owner(ct.author):
            #await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
            perms = ctx.author.permissions_in(ctx.channel).manage_messages
            await ctx.send(str(perms))

def setup(bot):
    bot.add_cog(Test(bot))
