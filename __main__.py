import os
import discord
from environs import Env
from discord.ext import commands
from dataclasses import dataclass

description = """
Your description here
""" 

bot = commands.Bot\
(
    command_prefix="plz ",
    description=description,
)

### User configuration
env = Env()
env.read_env()

bot.authorized_ids = env.list("authorized_ids", subcast=int)
bot.authorized_guilds = env.list("authorized_guilds", subcast=int)

### Classses
@dataclass
class MessageInfo:
    author: discord.Member = discord.Embed.Empty
    content: str = discord.Embed.Empty
    created_at = discord.Embed.Empty
bot.MessageInfo = MessageInfo

@dataclass
class AvatarInfo:
    avatar_url: str = ''
bot.AvatarInfo = AvatarInfo

### Login info
@bot.listen('on_ready')
async def login():
    print('--------------')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')

    ### Loading
    bot.load_extension('utils') 
    bot.load_extension('admin')
    bot.load_extension('example')

### Running
bot.run(env.str('token')) 
