from discord.ext import commands
from udpy import UrbanClient

class Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('ud',))
    async def urbandict(self, ctx, *args):
        if args:
            word = ' '.join(args)
            client = UrbanClient()
            defs = client.get_definition(word)
            if defs:
                m = defs[0].definition + '\ne.g.: ' + defs[0].example
                await ctx.send(m.replace('[','').replace(']',''))
            else:
                await ctx.send(f'No definition found for {word}')

def setup(bot):
    bot.add_cog(Stuff(bot))
