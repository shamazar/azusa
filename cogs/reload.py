from discord.ext import commands
import logging

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, *args):
        if self.bot.is_owner(ctx.author):
            if len(args) == 1:
                ext = args[0]
                if ext in self.bot.cogs.keys():
                    await ctx.send(f'Reloading {ext}...')
                    logging.warn(f'{ext} reloaded by {ctx.author}')
                    self.bot.reload_extension(f'cogs.{ext.lower()}')
                else:
                    await ctx.send(f'{ext} not recognised.')    


def setup(bot):
    bot.add_cog(Reload(bot))