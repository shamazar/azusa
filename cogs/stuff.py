from discord.ext import commands
from configparser import ConfigParser
from udpy import UrbanClient
from google_images_search import GoogleImagesSearch

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

    @commands.command(aliases=('img',))
    async def image(self, ctx, *args):
        if args:
            search = {
                'q': ' '.join(args),
                'num': 1,
                'safe': 'off',
                }

            # TODO: move to only loading keys on cog load, this is bad
            config = ConfigParser()
            config.read('bot.cfg')
            if config['google']['api_key'] and config['google']['engine_id']:
                key = config['google']['api_key']
                cx = config['google']['engine_id']
            else:
                return

            gis = GoogleImagesSearch(key, cx)
            gis.search(search_params=search)
            await ctx.send(gis.results()[0]._url)

def setup(bot):
    bot.add_cog(Stuff(bot))
