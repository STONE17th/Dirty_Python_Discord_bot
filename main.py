import datetime
import os
import random
from datetime import timedelta
from Text import info as inf
from Text import tasks as tsk

import discord
import asyncio
from discord.ext import commands, tasks
from Classes.user import User
from Data import tests, id, roles

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    check_kick_data.start()
    print('On start')


@bot.event
async def on_member_join(member):
    guild = bot.get_guild(id.channel_id)
    embed_message = inf.welcome_msg(member, guild)
    await bot.get_channel(id.start_channel).send(embed=embed_message)
    await member.send(f'{inf.ls_msg(member)}')


@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(id.channel_id)
    embed_message = inf.remove_msg(member, guild)
    await bot.get_channel(id.start_channel).send(embed=embed_message)


@bot.command()
async def rules(ctx):
    await bot.get_channel(id.rules_id).send(embed=inf.rules_msg()[0])
    await bot.get_channel(id.rules_id).send(embed=inf.rules_msg()[1])
    await bot.get_channel(id.rules_id).send(embed=inf.rules_msg()[2])
    await bot.get_channel(id.rules_id).send(embed=inf.rules_msg()[3])
    await bot.get_channel(id.rules_id).send(embed=inf.rules_msg()[4])


@tasks.loop(hours=24.0)
async def check_kick_data():
    guild = bot.get_guild(id.channel_id)
    time_now = datetime.datetime.now()
    format = "%d.%m.%Y %H:%M:%S"
    for member in guild.members:
        if check_delay(member):
            if (time_now - timedelta(days=7)).strftime(format) > member.joined_at.strftime(format):
                await member.send(inf.kick_msg(member)[0])
            elif (time_now - timedelta(days=6)).strftime(format) > member.joined_at.strftime(format):
                await member.send(inf.kick_msg(member)[1])
            elif (time_now - timedelta(days=3)).strftime(format) > member.joined_at.strftime(format):
                await member.send(inf.kick_msg(member)[2])
            elif (time_now - timedelta(days=1)).strftime(format) > member.joined_at.strftime(format):
                await member.send(inf.kick_msg(member)[3])


def check_delay(member: discord.Member):
    if member.bot:
        return False
    else:
        for role in member.roles:
            if role.id == roles.role_cx3.get(2):
                return False
        return True


@bot.command(aliases=['инфо', 'помощь'])
async def info(ctx):
    me = User(ctx, bot)
    join_date = me.get_member().joined_at.timestamp()
    now_date = datetime.datetime.now().timestamp()
    delta = now_date - join_date
    for role in me.get_member().roles:
        if roles.role_cx3.get(2) == role:
            await ctx.author.send(inf.info_msg(ctx, delta)[0])
            break
    else:
        await ctx.author.send(inf.info_msg(ctx, delta)[1])

@bot.command()
async def task(ctx):
    me = User(ctx, bot)
    task_number = random.randint(1, len(tests.answer_py))
    user_task = tests.test_py.get(task_number)
    msg = await ctx.send(f"```{user_task}```")

    def check(user):
        return user.channel == ctx.channel and user.author == ctx.author

    try:
        message = await bot.wait_for('message', check=check, timeout=60)
    except asyncio.TimeoutError:
        return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} {tsk.out_of_time()}"))

    if message.content == str(tests.answer_py.get(task_number)):
        try:
            await message.delete()
        except:
            pass
        await me.get_member().add_roles(me.role(2))
        return await msg.edit(content=f'{ctx.author.mention} {tsk.task_solved()}')
    else:
        try:
            await message.delete()
        except:
            pass
        return await msg.edit(content=f'{ctx.author.mention} {tsk.task_failed}')


@bot.command(aliases=['я', 'Я'])
async def my_language(ctx, *args):
    me = User(ctx, bot)
    if str(args[0]).lower().startswith('п') or str(args[0]).lower().startswith('p'):
        await me.get_member().add_roles(me.language('python'))
    if str(args[0]).lower().startswith('д') or str(args[0]).lower().startswith('j'):
        await me.get_member().add_roles(me.language('java'))


@bot.command()
async def embed(ctx, color, title, *args):
    me = User(ctx, bot)
    if me.admin():
        text = ''
        for word in args:
            text += f'{word} '
        else:
            text = text[:-1]
        col = int(str(color).replace('#', ''), 16)
        embed_message = discord.Embed(color=col, title=title, description=f'{text}')
        await ctx.send(embed=embed_message)
        await delete_message(ctx)
    else:
        await ctx.send(f"У тебя нет доступа к этой команде")


@bot.command()
async def test(ctx):
    me = User(ctx, bot)
    print(me.get_member())


async def delete_message(ctx):
    try:
        await ctx.message.delete()
    except:
        pass


bot.run(os.getenv('TOKEN'))
