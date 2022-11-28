import datetime
import os
import random
from datetime import timedelta

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
    embed_message = discord.Embed(title="Добро пожаловать!",
                                  description=f'Привет, {member.mention}. Это Cru4 Code Crew Discord сервер\n'
                                              f'Население: {guild.member_count}\nЗагляни в ЛС, я там тебе кое-чего прислал',
                                  color=0x108001)
    await bot.get_channel(id.start_channel).send(embed=embed_message)
    await member.send(
        f'Привет, {member.name}! Рады видеть тебя на этом сервере в наших рядах. Основная цель этого сервера - обмен опытом среди '
        f'разработчиков и помощь другим менее опытным коллегам\n'
        f'Хочешь быть действительно полезен? Предлагай проекты, меняйся полезными ссылками, давай советы, да и просто общайся в '
        f'тексте и голосе\n'
        f'Главное не груби, не обсуждай политоту (понимаем, что в наше время это сложно, но всё же) и не ставь себя выше других\n'
        f'Поддерживай дружественную ламповую атмосферу :)\n'
        f'С уважением, админы сервера CRU4 CODE CREW'
        f'In CRUTCH we trust!')


@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(id.channel_id)
    embed_message = discord.Embed(title="Зафиксирован побег!",
                                  description=f'Нас покинул {member.mention}.\n'
                                              f'Нас осталось: {guild.member_count}\n'
                                              f'Оно и к лучшему, не так уж мы тебя и любили',
                                  color=0x8f1800)
    await bot.get_channel(id.start_channel).send(embed=embed_message)


@bot.command()
async def rules(ctx):
    rule1 = discord.Embed(title="NPC (Общие правила, без доступа)",
                          description=f'Особых правил нет. Просто не хамим, не переходим на личности, не обсуждаем политоту. Основная цель - совместное решение задач и обмен опытом. для получения минимального доступа - команда /task\n**ВАЖНО** Если пользователь не получает роль Public Static Main в течение недели с момента захода на сервер - то автоматически исключается с сервера',
                          color=0xcfcfcf)
    rule2 = discord.Embed(title="Public Static Main (Зеленый доступ)",
                          description=f'Доступ к основным голосовым каналам по Пайтону и Джаве. Доступ к "библиотекам" с материалами и ссылками. Доступ можно получить командой /task',
                          color=0x0ba100)
    rule3 = discord.Embed(title="Кра4Кодер (Синий доступ)",
                          description=f'Доступ к голосовым канала по Пайтон и Джава. Решаем дополнительные задачи и реализуем пет-проекты. Доступ можно получить по подписке на Boosty',
                          color=0x062cc4)
    rule4 = discord.Embed(title="while (True): (Фиолетовый доступ)",
                          description=f'Возможность заходить на стрим в голосовом режиме и демонстрацией экрана, так же доступ к записям всех стримов. Доступ можно получить по подписке на Boosty',
                          color=0x690191)
    rule5 = discord.Embed(title="Админ (Оранжевый доступ)",
                          description=f'По поводу всех вопросов на сервере к людям с этой ролью. Предложения по продвижению и прочим орг.вопросам тоже к ним',
                          color=0xe69a02)
    await bot.get_channel(id.rules_id).send(embed=rule1)
    await bot.get_channel(id.rules_id).send(embed=rule2)
    await bot.get_channel(id.rules_id).send(embed=rule3)
    await bot.get_channel(id.rules_id).send(embed=rule4)
    await bot.get_channel(id.rules_id).send(embed=rule5)


@tasks.loop(hours=24.0)
async def check_kick_data():
    guild = bot.get_guild(id.channel_id)
    time_now = datetime.datetime.now()
    format = "%d.%m.%Y %H:%M:%S"
    for member in guild.members:
        if check_delay(member):
            if (time_now - timedelta(days=7)).strftime(format) > member.joined_at.strftime(format):
                await member.send(
                    f'{member.name}! Всё, пока! Доигрался!')
            elif (time_now - timedelta(days=6)).strftime(format) > member.joined_at.strftime(format):
                await member.send(
                    f'{member.name}, завтра мы с тобой попрощаемся, если... ну ты в курсе. Команда /task')
            elif (time_now - timedelta(days=3)).strftime(format) > member.joined_at.strftime(format):
                await member.send(
                    f'{member.name}, осталось 4 дня! Получай доступ скорее! Команда /task')
            elif (time_now - timedelta(days=1)).strftime(format) > member.joined_at.strftime(format):
                await member.send(
                    f'{member.name} есть еще 6 дней, чтобы получить минимальный доступ. Используй команду /task')


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
            await ctx.author.send(f'Привет, {(ctx.author.mention)}! Ты уже получил роль с минимальным доступом и можешь '
                                  f'находится на сервере бессрочно :) Из доступных тебе команд у тебя пока только всё '
                                  f'та же команда /task (можешь порешать другие задачи, результат выполнения ни на что '
                                  f'не повлияет.\nБот постоянно развивается и функционал будет допиливаться\n'
                                  f'Если есть предложения по продвижению бота и сервера - пиши кому-нибудь из админов')
            break
    else:
        await ctx.author.send(
            f'Привет, {(ctx.author.mention)}! В первую очередь тебе надо получить роль минимального доступа. Для этого '
            f'в текстовом чате введи команду /task и реши небольшую задачку (да, да, как на CodeWars)\n'
            f'Если этого не сделать то ,через '
            f'{timedelta(days=7) - timedelta(seconds=int(delta))} '
            f'ты будешь изгнан из сервера (без позора, но тоже не приятно')

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
        return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention} Время вышло!"))

    if message.content == str(tests.answer_py.get(task_number)):
        try:
            await message.delete()
        except:
            pass
        await me.get_member().add_roles(me.role(2))
        return await msg.edit(content=f'{ctx.author.mention} Вы прошли проверку')
    else:
        try:
            await message.delete()
        except:
            pass
        return await msg.edit(content=f'{ctx.author.mention} Вы не прошли проверку')


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
