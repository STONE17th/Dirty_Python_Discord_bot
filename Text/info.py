import discord
from random import choice 


def welcome_msg(member, guild):
    descr_hi = [f'Привет, {member.mention}.\n', f'Мы рады видеть тебя, {member.mention}.\n',
    f'Рады тебя видеть, {member.mention}.\n', f'Здравствуй, {member.mention}.\n', f'Приветствую, {member.mention}.\n']
    descr_ccc = ['Это Cru4 Code Crew Discord сервер\n', 'Это Discord-сервер "Cru4 Code Crew"\n',
    'Ты попал на Discord-сервер "Cru4 Code Crew"\n', 'Сейчас ты на Discord-сервере "Cru4 Code Crew\n']
    descr_count = [f'Население: {guild.member_count}\n', f'На данный момент наше население: {guild.member_count}\n', 
    f'По данным последней переписи, наше население: {guild.member_count}\n', f'Сейчас наше население: {guild.member_count}\n']
    descr_ls = ['Загляни в ЛС, я там тебе кое-чего прислал', 'Я кое-что написал тебе в ЛС. Проверь ;)', 
    'Проверь ЛС. Я написал тебе кое-что', 'Я отправил тебе важное сообщение в ЛС. Проверь, пожалуйста']
    
    descript = f'{choice(descr_hi)}{choice(descr_ccc)}{choice(descr_count)}{choice(descr_ls)}'
    ttl = choice(['Добро пожаловать!', 'Посмотрите кто пришёл!', 'Вот это встреча!'])
    msg = discord.Embed(title=f"{ttl}", description=f'{descript}', color=0x108001)

    return msg
    
def ls_msg(member):
    msg = f'Привет, {member.name}! Рады видеть тебя на этом сервере в наших рядах. Основная цель этого сервера - обмен опытом среди\
разработчиков и помощь другим менее опытным коллегам\
Хочешь быть действительно полезен? Предлагай проекты, меняйся полезными ссылками, давай советы, да и просто общайся в\
тексте и голосе\
Главное не груби, не обсуждай политоту (понимаем, что в наше время это сложно, но всё же) и не ставь себя выше других\
Поддерживай дружественную ламповую атмосферу :)\
С уважением, админы сервера CRU4 CODE CREW\
In CRUTCH we trust!'
    return msg

def remove_msg(member, guild):
    ttl = choice(['Зафиксирован побег!', 'Кажется, у нас потери!', 'Мы кое-кого потеряли!'])
    descr_bye = choice(['Оно и к лучшему, не так уж мы тебя и любили', 
'Будешь вспоминать нас и жалеть о содеянном', 'Может ещё встретимся. А может и нет'])
    msg = discord.Embed(title=f"{ttl}",
        description=f'Нас покинул {member.mention}.\n'
                    f'Нас осталось: {guild.member_count}\n'
                    f'{descr_bye}', color=0x8f1800)
    return msg

def out_of_time():
    msg = choice(["Время вышло!", "Надо бы побыстрее. Время вышло!",
"Время вышло! Попробуй ещё раз, но порасторопнее"])
    return msg

def task_solved():
    msg = choice(["Так держать! Проверка пройдена", "Проверка пройдена!",
"Проверка успешно пройдена", "Вы прошли проверку!", "Поздравляю! Вы успешно прошли проверку"])
    return msg

def task_failed():
    msg = choice(["Проверка провалена", "Вы не прошли проверку",
"Проверка не пройдена", "Вы успешно не прошли проверку"])
    return msg