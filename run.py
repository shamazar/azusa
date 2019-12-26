#!/usr/bin/env python
import discord
from discord.ext import commands

import os
import logging
from configparser import ConfigParser

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    if os.path.isfile('bot.cfg'):
        config = ConfigParser()
        config.read('bot.cfg')
    else:
        raise OSError("bot.cfg not found")

    bot = commands.Bot(config['bot']['prefix'])
    bot.owner_id = int(config['bot']['ownerid'])

    for cog in os.listdir('cogs'):
        if cog.endswith('.py'):
            name = cog[:-3]
            bot.load_extension(f'cogs.{name}')

    bot.run(config['bot']['token'])
