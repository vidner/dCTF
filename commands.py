from discord.ext import commands
from handlers import team_controller, task_controller, audit_controller, view_controller

import config

def start():

    bot = commands.Bot(command_prefix='>>')

    @bot.command(name='register', help='Register your team.')
    async def register(ctx, team: str):
        response = team_controller.register(team)
        await ctx.send(response)

    @bot.command(name='login', help='Login with team token.')
    async def login(ctx, token: str):
        response = team_controller.login(str(ctx.author.id), token)
        await ctx.send(response)
    
    @bot.command(name='create-task', help='Create a challenges.')
    @commands.has_role(config.credential.role)
    async def create_task(ctx, name: str, category: str, description: str, files: str, flag: str):
        response = task_controller.create_task(name, category, description, files, flag)
        await ctx.send(response)
    
    @bot.command(name='release-task', help='Release a challenges.')
    @commands.has_role(config.credential.role)
    async def release_task(ctx, task_id: int):
        response = task_controller.release_task(task_id)
        await ctx.send(response)

    @bot.command(name='hide-task', help='Hide a challenges.')
    @commands.has_role(config.credential.role)
    async def hide_task(ctx, task_id: int):
        response = task_controller.hide_task(task_id)
        await ctx.send(response)

    @bot.command(name='delete-task', help='Delete a challenges.')
    @commands.has_role(config.credential.role)
    async def delete_task(ctx, task_id: int):
        response = task_controller.delete_task(task_id)
        await ctx.send(response)
    
    @bot.command(name='submit', help='Submit flag.')
    async def submit(ctx, flag: str):
        response = audit_controller.submit(str(ctx.author.id), flag)
        await ctx.send(response)

    @bot.command(name='challenges', help='List all chalengges.')
    async def submit(ctx):
        response = view_controller.challenges()
        await ctx.send(embed=response)

    @bot.command(name='challenges-info', help='Get chalengges info.')
    async def submit(ctx, name: str):
        response = view_controller.challenges_info(name)
        await ctx.send(embed=response)

    @bot.command(name='scoreboard', help='1-10 Scoreboard.')
    async def submit(ctx):
        response = view_controller.scoreboard_before_freeze()
        await ctx.send(embed=response)

    bot.run(config.credential.token)