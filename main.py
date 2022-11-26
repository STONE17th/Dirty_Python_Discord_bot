import random

import discord
# from discord import client
from discord.ext import commands

from Classes.user import User


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('On start')


@bot.event
async def on_member_join(member):
    print(dir(member))
    print(member.roles)


@bot.command()
async def captcha(ctx):
    import asyncio
    captcha = random.randint(11111, 99999)
    msg = await ctx.send(
        f"\n```ПРОВЕРКА НА ВАШУ СКОРОСТЬ \nкод ниже \nкод ниже \n{captcha} \nкод выше \nкод выше \nПРОВЕРКА НА ВАШУ СКОРОСТЬ```")

    def check(message):
        return message.channel == ctx.channel and message.author == ctx.author

    try:
        message = await bot.wait_for('message', check=check, timeout=60)
    except asyncio.TimeoutError:
        return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} Время вышло!"))

    if message.content == str(captcha):
        await message.delete()
        return await msg.edit(content=f'{ctx.author.mention} Вы прошли проверку')
    else:
        await message.delete()
        return await msg.edit(content=f'{ctx.author.mention} Вы не прошли проверку')

@bot.command()
async def info(ctx):
    me = User(ctx, bot)
    me.from_db()
    me.show()
    me.role()


async def set_role(ctx):
    me = User(ctx, bot)
    await me.get_member().add_roles(me.role(2))


@bot.command()
async def role(ctx, *args):
    me = User(ctx, bot)
    if me.admin():
        await me.get_member().add_roles(me.role(int(args[0])))

@bot.command()
async def embed(ctx):
    me = User(ctx, bot)
    if me.admin():
        await ctx.send(f'{me.name} красавчик')
    else:
        await ctx.send('Пшлнх, самозванец')


bot.run('MTA0NTk5NDE0NDk1NjQxNjA0MA.GXasph.yMUIv0dm3Y15dITAtg__3nc3BU8buwFGUVncwk')
