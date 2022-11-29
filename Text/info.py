import discord
from random import choice
from datetime import timedelta


def welcome_msg(member, guild):
    descr_hi = [f'Привет, {member.mention}.\n', f'Мы рады видеть тебя, {member.mention}.\n',
                f'Рады тебя видеть, {member.mention}.\n', f'Здравствуй, {member.mention}.\n',
                f'Приветствую, {member.mention}.\n']
    descr_ccc = ['Это Cru4 Code Crew Discord сервер\n', 'Это Discord-сервер "Cru4 Code Crew"\n',
                 'Ты попал на Discord-сервер "Cru4 Code Crew"\n', 'Сейчас ты на Discord-сервере "Cru4 Code Crew\n']
    descr_count = [f'Население: {guild.member_count}\n', f'На данный момент наше население: {guild.member_count}\n',
                   f'По данным последней переписи, наше население: {guild.member_count}\n',
                   f'Сейчас наше население: {guild.member_count}\n']
    descr_ls = ['Загляни в ЛС, я там тебе кое-чего прислал', 'Я кое-что написал тебе в ЛС. Проверь ;)',
                'Проверь ЛС. Я написал тебе кое-что', 'Я отправил тебе важное сообщение в ЛС. Проверь, пожалуйста']
    descript = f'{choice(descr_hi)}{choice(descr_ccc)}{choice(descr_count)}{choice(descr_ls)}'
    ttl = choice(['Добро пожаловать!', 'Посмотрите кто пришёл!', 'Вот это встреча!'])
    msg = discord.Embed(title=f"{ttl}", description=f'{descript}', color=0x108001)
    return msg


def ls_msg(member):
    msg = f'Привет, {member.name}! Рады видеть тебя на этом сервере в наших рядах.\n' \
          f'Основная цель этого сервера - обмен опытом среди разработчиков и помощь другим менее опытным коллегам.\n' \
          f'Хочешь быть действительно полезен? Предлагай проекты, меняйся полезными ссылками, давай советы, ' \
          f'да и просто общайся в тексте и голосе.\n' \
          f'Главное не груби, не обсуждай политоту (понимаем, что в наше время это сложно, но всё же) и не ставь себя ' \
          f'выше других.\n' \
          f'Поддерживай дружественную ламповую атмосферу :)\n' \
          f'С уважением, админы сервера CRU4 CODE CREW\n' \
          f'In CRUTCH we trust!\n'
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


def rules_msg():
    rule1 = discord.Embed(title="NPC (Общие правила, без доступа)",
                          description=f'Особых правил нет. Просто не хамим, не переходим на личности, не обсуждаем '
                                      f'политоту. Основная цель - совместное решение задач и обмен опытом. для '
                                      f'получения минимального доступа - команда /task\n**ВАЖНО** Если пользователь '
                                      f'не получает роль Public Static Main в течение недели с момента захода на '
                                      f'сервер - то автоматически исключается с сервера',
                          color=0xcfcfcf)
    rule2 = discord.Embed(title="Public Static Main (Зеленый доступ)",
                          description=f'Доступ к основным голосовым каналам по Пайтону и Джаве. Доступ к '
                                      f'"библиотекам" с материалами и ссылками. Доступ можно получить командой /task',
                          color=0x0ba100)
    rule3 = discord.Embed(title="Кра4Кодер (Синий доступ)",
                          description=f'Доступ к голосовым канала по Пайтон и Джава. Решаем дополнительные задачи и '
                                      f'реализуем пет-проекты. Доступ можно получить по подписке на Boosty',
                          color=0x062cc4)
    rule4 = discord.Embed(title="while (True): (Фиолетовый доступ)",
                          description=f'Возможность заходить на стрим в голосовом режиме и демонстрацией экрана, '
                                      f'так же доступ к записям всех стримов. Доступ можно получить по подписке на '
                                      f'Boosty',
                          color=0x690191)
    rule5 = discord.Embed(title="Админ (Оранжевый доступ)",
                          description=f'По поводу всех вопросов на сервере к людям с этой ролью. Предложения по '
                                      f'продвижению и прочим орг.вопросам тоже к ним',
                          color=0xe69a02)
    rules = [rule1, rule2, rule3, rule4, rule5]
    return rules


def kick_msg(member):
    msg = ['Всё, пока! Доигрался!',
           f'{member.name}, завтра мы с тобой попрощаемся, если... ну ты в курсе. Команда /task',
           f'{member.name}, осталось 4 дня! Получай доступ скорее! Команда /task',
           f'{member.name} есть еще 6 дней, чтобы получить минимальный доступ. Используй команду /task']
    return msg


def info_msg(ctx, delta):
    msg1 = f'Привет, {ctx.author.mention}! Ты уже получил роль с минимальным доступом и можешь находится на сервере ' \
           f'бессрочно :) Из доступных тебе команд у тебя пока только всё та же команда /task (можешь порешать ' \
           f'другие задачи, результат выполнения ни на что не повлияет. Бот постоянно развивается и функционал будет ' \
           f'допиливаться. Если есть предложения по продвижению бота и сервера - пиши кому-нибудь из админов '
    msg2 = f'Привет, {ctx.author.mention}!\
В первую очередь тебе надо получить роль минимального доступа.\
Для этого в текстовом чате введи команду /task и реши небольшую задачку (да, да, как на CodeWars)\
Если этого не сделать то ,через {timedelta(days=7) - timedelta(seconds=int(delta))} ты будешь изгнан из сервера (без ' \
           f'позора, но тоже не приятно) '
    msg = [msg1, msg2]
    return msg


def time_to_die(member):
    ttl = choice(["Тик-так", "Часики тикают", "Время идёт"])
    descr_6days = choice([f'{member.name} есть еще 6 дней, чтобы получить минимальный доступ. Используй команду /task'])
    descr_5days = choice([f'{member.name} у тебя еще 5 дней, чтобы получить доступ. Используй команду /task'])
    descr_4days = choice([f'{member.name}, осталось 4 дня! Получай доступ скорее! Команда /task'])
    descr_3days = choice([f'{member.name}, осталось 3 дня! Просто реши задачу! Команда /task'])
    descr_2days = choice([f'{member.name}, осталось 2 дня! Времени почти не осталось! Команда /task'])
    descr_1day = choice([f'{member.name}, завтра мы с тобой попрощаемся, если... ну ты в курсе. Команда /task'])
    descr_bye = choice([f'Пока, {member.name}! Доигрался!'])
    six_days = discord.Embed(title=f"{ttl}",
                             description=f'{descr_6days}',
                             color=0xFFFF00)
    five_days = discord.Embed(title=f"{ttl}",
                              description=f'{descr_5days}',
                              color=0xFFFF00)
    four_days = discord.Embed(title=f"{ttl}",
                              description=f'{descr_4days}',
                              color=0xFFFF00)
    three_days = discord.Embed(title=f"{ttl}",
                               description=f'{descr_3days}',
                               color=0xFFFF00)
    two_days = discord.Embed(title=f"{ttl}",
                             description=f'{descr_2days}',
                             color=0xFFFF00)
    one_day = discord.Embed(title=f"{ttl}",
                            description=f'{descr_1day}',
                            color=0xFFFF00)
    bye_bye = discord.Embed(title="Вот и всё!",
                            description=f'{descr_bye}!',
                            color=0x8f1800)
    msg = [bye_bye, one_day, two_days, three_days, four_days, five_days, six_days]
    return msg
