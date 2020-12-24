

from config import get_config
from discord.ext import commands
from handlers import team_controller


def start():

    bot = commands.Bot(command_prefix='>>')
    config = get_config()

    @bot.command(name='register', help='Register your team.')
    async def register(ctx, teamname: str):
        response = team_controller.register(teamname, config.credential.secret)
        await ctx.send(response)

    @bot.command(name='login', help='Login with team token.')
    async def login(ctx, token: str):
        response = team_controller.login(str(ctx.author.id), token, config.credential.secret)
        await ctx.send(response)

    bot.run(config.credential.token)