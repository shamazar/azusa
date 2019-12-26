from discord.ext import commands

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, *args):
        if self.bot.is_owner(ctx.author):
            if not args:
                async with ctx.channel.typing():
                    for cog in self.bot.cogs.keys():
                        self.bot.reload_extension(f'cogs.{cog.lower()}')
                    await ctx.send(f'{len(self.bot.cogs)} cogs reloaded.')

            elif len(args) == 1:
                cog = args[0]
                if cog in self.bot.cogs.keys():
                    await ctx.send(f'Reloading {cog}...')
                    self.bot.reload_extension(f'cogs.{cog.lower()}')
                else:
                    await ctx.send(f'{cog} not recognised.')

            else:
                await ctx.send('Unrecognised arguments, please specify a cog.')
    
    @commands.command()
    async def listcogs(self, ctx):
        if self.bot.is_owner(ctx.author):
            await ctx.send(', '.join(self.bot.cogs.keys()))

def setup(bot):
    bot.add_cog(Reload(bot))