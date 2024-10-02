import discord
import os
import json
import random
import asyncio
import config
import time
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import requests

intents = discord.Intents.default()
intents.members = True  # если нужно отслеживать участников
intents.message_content = True  # для получения содержания сообщений
intents.reactions = True  # Для работы с реакциями

BOT = commands.Bot(command_prefix=config.SETTINGS['PREFIX'], intents=intents)
BOT.remove_command('help')


@BOT.command()
@commands.has_permissions(administrator=True)
async def test(payload):
    await payload.member.channel.send(f'{payload.member.author.roles}')
    if 'Админушка' in f'{payload.member.author.roles}':
        await payload.member.channel.send(f'{payload.member.author.roles[len(payload.member.author.roles) - 4]}')
    else:
        await payload.member.channel.send(f'{payload.member.author.roles[len(payload.member.author.roles) - 3]}')


@BOT.command()
@commands.has_permissions(administrator=True)
async def one(ctx, value1=0, value2=0, value3=0, value4=0):
    # Первое сообщение
    if value1 == 1:
        emb = discord.Embed(title='Правила / заметки:', colour=discord.Color.green())
        emb.add_field(name='Маты запрещены! (Но боту можно)', value='Бот просто удалит сообщение, где используется мат.', inline=False)
        emb.add_field(name='Не пытайтесь перегружайте бота, ему и так сложно работать.', value='Он стоит на костылях...', inline=False)
        emb.add_field(name='Бот не всегда в сети, и не всегда работает.', value='Ему тоже нужен отдых.', inline=False)
        emb.add_field(name='Первым делом выбираем ваши ранги и персонажей (только честно).', value='Только после этого станет доступна остальная часть канала!', inline=False)
        emb.add_field(name='Меняем ники на метку#id в Валоранте:', value='KreO#HML', inline=False)
        emb.add_field(name='Наслаждаемся времяприпровождением!', value='Или уходите!', inline=False)
        await ctx.send(embed=emb)

    # Второе сообщение
    if value2 == 1:
        emb = discord.Embed(title='Для получения роли (ранг) оставте реакцию к этому сообщению:', colour=discord.Color.green())
        emb.add_field(name='Без ранга', value=':white_circle:', inline=True)
        emb.add_field(name='Железо', value='<:fer:777860907673059328>', inline=True)
        emb.add_field(name='Бронза', value='<:bronze:777860907651956767>', inline=True)
        emb.add_field(name='Серебро', value='<:silver:777860908063785010>', inline=True)
        emb.add_field(name='Золото', value='<:gold:777860908021448724>', inline=True)
        emb.add_field(name='Платина', value='<:platinium:777860907979767830>', inline=True)
        emb.add_field(name='Алмаз', value='<:diamond:777860908038619147>', inline=True)
        emb.add_field(name='Бессмертный', value='<:immortal:777860907958796311>', inline=True)
        emb.add_field(name='Радиант', value='<:radiant:777860907992481802>', inline=True)
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('⚪')
        await msg.add_reaction('<:fer:777860907673059328>')
        await msg.add_reaction('<:bronze:777860907651956767>')
        await msg.add_reaction('<:silver:777860908063785010>')
        await msg.add_reaction('<:gold:777860908021448724>')
        await msg.add_reaction('<:platinium:777860907979767830>')
        await msg.add_reaction('<:diamond:777860908038619147>')
        await msg.add_reaction('<:immortal:777860907958796311>')
        await msg.add_reaction('<:radiant:777860907992481802>')

    # Третье сообщение
    if value3 == 1:
        emb = discord.Embed(title='Так же следует оставить реакцию под этим сообщением:', colour=discord.Color.green())
        emb.add_field(name='Ранг 1', value='1️⃣', inline=True)
        emb.add_field(name='Ранг 2', value='2️⃣', inline=True)
        emb.add_field(name='Ранг 3', value='3️⃣', inline=True)
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')

    # Четвёртое сообщение
    if value4 == 1:
        emb = discord.Embed(title='Для получения роли (персонаж) оставте реакцию к этому сообщению:', colour=discord.Color.green())
        emb.add_field(name='Jett', value='<:jett:777960703326683167>', inline=True)
        emb.add_field(name='Raze', value='<:raze:777960704182976512>', inline=True)
        emb.add_field(name='Breach', value='<:breach:777960704459669524>', inline=True)
        emb.add_field(name='Omen', value='<:omen:777960704157810769>', inline=True)
        emb.add_field(name='Brimstone', value='<:brim:777960704350093342>', inline=True)
        emb.add_field(name='Phoenix', value='<:phoe:777960703109234760>', inline=True)
        emb.add_field(name='Sage', value='<:sage:777960704220332032>', inline=True)
        emb.add_field(name='Sova', value='<:sova:777960703859490916>', inline=True)
        emb.add_field(name='Viper', value='<:viper:777960704468582450>', inline=True)
        emb.add_field(name='Cypher', value='<:cypher:777960703763808258>', inline=True)
        emb.add_field(name='Reyna', value='<:reyna:777960704148766720>', inline=True)
        emb.add_field(name='Killjoy', value='<:killjoy:777960704056623207>', inline=True)
        emb.add_field(name='Skye', value='⚪', inline=True)
        emb.add_field(name='Если вы ошиблись в выборе персонажа или хотите его поменять, поставте эту реакцию:', value='🔴', inline=False)
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('<:jett:777960703326683167>')
        await msg.add_reaction('<:raze:777960704182976512>')
        await msg.add_reaction('<:breach:777960704459669524>')
        await msg.add_reaction('<:omen:777960704157810769>')
        await msg.add_reaction('<:brim:777960704350093342>')
        await msg.add_reaction('<:phoe:777960703109234760>')
        await msg.add_reaction('<:sage:777960704220332032>')
        await msg.add_reaction('<:sova:777960703859490916>')
        await msg.add_reaction('<:viper:777960704468582450>')
        await msg.add_reaction('<:cypher:777960703763808258>')
        await msg.add_reaction('<:reyna:777960704148766720>')
        await msg.add_reaction('<:killjoy:777960704056623207>')
        await msg.add_reaction('⚪')
        await msg.add_reaction('🔴')


# Бот подключился
@BOT.event
async def on_ready():
    print(f"Logged on as {config.SETTINGS['BOT']}!")
    await BOT.change_presence(status=discord.Status.online, activity=discord.Game(f'{config.SETTINGS["PREFIX"]}help'))


# Новая инвайт ссылка
@BOT.event
async def on_invite_create(invite):
    time = invite.max_age // 60
    if invite.max_uses == 0:
        uses = 'Без ограничений'
    else:
        uses = f'{invite.max_uses}'
    if time == 0:
        use_time = 'Никогда'
    elif time > 30:
        time = time // 60
        use_time = f'{time} час'
        if time == 24:
            use_time = use_time + 'a'
        elif time > 1:
            use_time = use_time + 'ов'
    else:
        use_time = '30 минут'
    emb = discord.Embed(title=f'{invite.inviter} создал ссылку для приглашения на сервер {invite.guild}!', colour=discord.Color.red())
    emb.add_field(name=f'Новая ссылка: '.format(config.SETTINGS['PREFIX']), value=f'{invite}', inline=False)
    emb.add_field(name=f'Количество переходов: '.format(config.SETTINGS['PREFIX']), value=f'{uses}', inline=False)
    emb.add_field(name=f'Срок действия истекает через: '.format(config.SETTINGS['PREFIX']), value=f'{use_time}', inline=False)
    emb.add_field(name=f'Временное членство: '.format(config.SETTINGS['PREFIX']), value=f'{invite.temporary}', inline=False)
    try:
        message = await invite.channel.send(embed=emb)
        print(f'New invite link: {invite}')
        await asyncio.sleep(300)
        await message.delete()
    except Exception:
        print('Error_in_invite')


# Бот зашел на сервер
@BOT.event
async def on_guild_join(guild):
    category = guild.categories[0]
    channel = category.channels[0]
    await channel.send('Приветствую! Я - новый бот этого сервера: {}! \n'
                       'Если есть идеи для доработки бота, или вы нашли баг - пишите, не стесняйтесь!'.format(guild.name))


# Выдача роли по реакции к сообщению
@BOT.event
async def on_raw_reaction_remove(payload):
    member = get(BOT.get_all_members(), id=payload.user_id)
    # Персонажи
    if payload.message_id == config.SETTINGS['CHARACTER_REACTION_MESSAGE_ID']:
        for guild in BOT.guilds:
            try:
                if '_РАНГ_' in f'{member.roles}':
                    role = discord.utils.get(guild.roles, name='Сервер доступен!')
                    if 'None' not in f'{role}':
                        await member.remove_roles(role)
                else:
                    role = discord.utils.get(guild.roles, name=config.ROLES_CHARACTER[payload.emoji.name])
                    if 'None' not in f'{role}':
                        await member.remove_roles(role)
                        print(f'User [{member}] loss role [{role}]')
            except Exception:
                print(f'Some problems in [role CHARACTER with reaction]...')


# Выдача роли по реакции к сообщению
@BOT.event
async def on_raw_reaction_add(payload):
    # Ранги
    if payload.message_id == config.SETTINGS['RANK_REACTION_MESSAGE_ID']:
        for guild in BOT.guilds:
            try:
                role = discord.utils.get(guild.roles, name='______________РАНГ______________')
                if 'None' not in f'{role}':
                    await payload.member.add_roles(role)
                if '_ПЕРСОНАЖИ_' in f'{payload.member.roles}':
                    role = discord.utils.get(guild.roles, name='Сервер доступен!')
                    if 'None' not in f'{role}':
                        await payload.member.add_roles(role)
                for i in range(0, len(config.ROLES_WORDS_RANK_NAME)):
                    role = discord.utils.get(guild.roles, name=config.ROLES_WORDS_RANK_NAME[i])
                    if ('None' not in f'{role}') and f'{role.name}' in f'{payload.member.roles}':
                        await payload.member.remove_roles(role)
                    if role != discord.utils.get(guild.roles, name=config.ROLES_RANK[payload.emoji.name]):
                        await BOT.http.remove_reaction(payload.channel_id, payload.message_id, config.ROLES_WORDS_RANK_EMOJI[i], payload.user_id)
                role = discord.utils.get(guild.roles, name=config.ROLES_RANK[payload.emoji.name])
                if 'None' not in f'{role}':
                    await payload.member.add_roles(role)
                    print(f'User [{payload.member}] get role [{role}]')
            except Exception:
                print(f'Some problems in [role RANK with reaction]...')

    # Номера рангов
    if payload.message_id == config.SETTINGS['NUM_REACTION_MESSAGE_ID']:
        for guild in BOT.guilds:
            try:
                for i in range(0, 3):
                    role = discord.utils.get(guild.roles, name=config.ROLES_WORDS_NUM_NAME[i])
                    if ('None' not in f'{role}') and f'{role.name}' in f'{payload.member.roles}':
                        await payload.member.remove_roles(role)
                    if role != discord.utils.get(guild.roles, name=config.ROLES_NUM[payload.emoji.name]):
                        await BOT.http.remove_reaction(payload.channel_id, payload.message_id, config.ROLES_WORDS_NUM_EMOJI[i], payload.user_id)
                role = discord.utils.get(guild.roles, name=config.ROLES_NUM[payload.emoji.name])
                if 'None' not in f'{role}':
                    await payload.member.add_roles(role)
                    print(f'User [{payload.member}] get role [{role}]')
            except Exception:
                print(f'Some problems in [role NUM with reaction]...')

    # Персонажи
    if payload.message_id == config.SETTINGS['CHARACTER_REACTION_MESSAGE_ID']:
        for guild in BOT.guilds:
            try:
                role = discord.utils.get(guild.roles, name='__________ПЕРСОНАЖИ__________')
                if 'None' not in f'{role}':
                    await payload.member.add_roles(role)
                if '_РАНГ_' in f'{payload.member.roles}':
                    role = discord.utils.get(guild.roles, name='Сервер доступен!')
                    if 'None' not in f'{role}':
                        await payload.member.add_roles(role)
                else:
                    role = discord.utils.get(guild.roles, name=config.ROLES_CHARACTER[payload.emoji.name])
                    if 'None' not in f'{role}':
                        await payload.member.add_roles(role)
                        print(f'User [{payload.member}] get role [{role}]')
            except Exception:
                print(f'Some problems in [role CHARACTER with reaction]...')


# Изменение людей в гс каналах
@BOT.event
async def on_voice_state_update(member, before, after):
    print(f'[{member}] go to [{after.channel}] from [{before.channel}]')
    channel = '0'
    # Создание канала, изменение инфы о мемберах в войс каналах
    if member.guild.id == 766724993203437578:
        if (f'{after.channel}' != 'None'):
            if f'{before.channel}' == 'None':
                members_in_voice = 0
                for i in range(0, len(member.guild.voice_channels) - 1):
                    members_in_voice = members_in_voice + len(member.guild.voice_channels[i].members)
                infocategory = discord.utils.get(member.guild.categories, id=config.SETTINGS['CHANNEL_INFO_GROUP_ID'])
                await member.guild.create_voice_channel(name=f'В голосовых каналах: {members_in_voice}', category=infocategory)
                for i in range(0, len(member.guild.voice_channels) - 1):
                    if 'В голосовых каналах: ' in f'{member.guild.voice_channels[i]}':
                        await member.guild.voice_channels[i].delete()
                print(f'In voice [{members_in_voice}]')
            if after.channel.id == config.SETTINGS['CREATE_WITH_CHANNEL_ID']:
                for guild in BOT.guilds:
                    maincategory = discord.utils.get(guild.categories, id=config.SETTINGS['CREATE_TO_GROUP_ID'])
                    if 'Админушка' in f'{member.roles}':
                        channel_new = await guild.create_voice_channel(name=f'{member.roles[len(member.roles) - 4]} {member.roles[len(member.roles) - 5]}', category=maincategory, user_limit=0)
                    else:
                        channel_new = await guild.create_voice_channel(name=f'{member.roles[len(member.roles) - 3]} {member.roles[len(member.roles) - 4]}', category=maincategory, user_limit=0)
                    await channel_new.set_permissions(member, connect=True, mute_members=True, move_members=True, manage_channels=True)
                    try:
                        await member.move_to(channel_new)

                        def check(x, y, z):
                            return len(channel_new.members) == 0

                        await BOT.wait_for('voice_state_update', check=check)
                        await channel_new.delete()
                    except Exception:
                        print('Voice_channel_error!')
        else:
            members_in_voice = 0
            for i in range(0, len(member.guild.voice_channels) - 1):
                members_in_voice = members_in_voice + len(member.guild.voice_channels[i].members)
            infocategory = discord.utils.get(member.guild.categories, id=config.SETTINGS['CHANNEL_INFO_GROUP_ID'])
            await member.guild.create_voice_channel(name=f'В голосовых каналах: {members_in_voice}', category=infocategory)
            for i in range(0, len(member.guild.voice_channels) - 1):
                if 'В голосовых каналах: ' in f'{member.guild.voice_channels[i].name}':
                    await member.guild.voice_channels[i].delete()
            print(f'In voice [{members_in_voice}]')


# Помощь по командам
@BOT.command()
async def help(ctx, value='all'):
    emb = ''
    # Группы
    if value == 'all':
        emb = discord.Embed(title='Доступные группы команд:', colour=discord.Color.green())
        emb.add_field(name=f'{config.SETTINGS["PREFIX"]}help funny', value='Рандомные картинки животных', inline=False)
        emb.add_field(name=f'{config.SETTINGS["PREFIX"]}help other', value='Разные команды (это просто надо видеть)', inline=False)
        emb.add_field(name=f'{config.SETTINGS["PREFIX"]}help admin', value='Админские команды', inline=False)

    # Рандомные картинки
    if value == 'funny':
        emb = discord.Embed(title='Команды рандомных картинок животных:', colour=discord.Color.green())
        emb.add_field(name='{}dog'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка собакена', inline=False)
        emb.add_field(name='{}cat'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка котика', inline=False)
        emb.add_field(name='{}pand'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка панды', inline=False)
        emb.add_field(name='{}red_pand'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка красной панды', inline=False)
        emb.add_field(name='{}bird'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка птицы', inline=False)
        emb.add_field(name='{}fox'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка лисы', inline=False)
        emb.add_field(name='{}koala'.format(config.SETTINGS['PREFIX']), value='Рандомная картинка коалы', inline=False)

    # Прикольные
    if value == 'other':
        emb = discord.Embed(title='Другие команды:', colour=discord.Color.green())
        emb.add_field(name='{}hug'.format(config.SETTINGS['PREFIX']), value='Обнимашки', inline=False)
        emb.add_field(name='{}ping'.format(config.SETTINGS['PREFIX']), value='Ваш пинг (5 ~ 500, def = 50)', inline=False)
        emb.add_field(name='{}link'.format(config.SETTINGS['PREFIX']), value='Ссылка для приглашения друзей на этот сервер', inline=False)
        emb.add_field(name='{}help'.format(config.SETTINGS['PREFIX']), value='Эта команда', inline=False)
        emb.add_field(name='{}info'.format(config.SETTINGS['PREFIX']), value='Информация о @пользователе', inline=False)
        emb.add_field(name='{}donate'.format(config.SETTINGS['PREFIX']), value='Донат разработчику / связь с ним', inline=False)
        emb.add_field(name='{}site'.format(config.SETTINGS['PREFIX']), value='Ссылка на сайт (def = youtube)', inline=False)

    # Админские
    if value == 'admin':
        emb = discord.Embed(title='Админские команды:', colour=discord.Color.green())
        emb.add_field(name='{}clear'.format(config.SETTINGS['PREFIX']), value='Очистить чат (def = 10)', inline=False)
        emb.add_field(name='{}kick'.format(config.SETTINGS['PREFIX']), value='Кикнуть пользователя', inline=False)
        emb.add_field(name='{}ban'.format(config.SETTINGS['PREFIX']), value='Забанить пользователя', inline=False)
        emb.add_field(name='{}unban'.format(config.SETTINGS['PREFIX']), value='Разбанить пользователя', inline=False)
        emb.add_field(name='{}give'.format(config.SETTINGS['PREFIX']), value='Дать роль пользователю (@пользователь @роль)', inline=False)
        emb.add_field(name='{}remove'.format(config.SETTINGS['PREFIX']), value='Отнять роль у пользователя (@пользователь @роль)', inline=False)

    await ctx.send(embed=emb)


# В сообщении
@BOT.event
async def on_message(message):
    await BOT.process_commands(message)
    msg = message.content.lower()

    # Использование команд
    for i in range(0, len(config.ALL_COMMANDS)):
        if config.ALL_COMMANDS[i] in msg:
            print(f'[{message.author}] used command [{msg}]')

    # Рандом картинки животных
    if msg in config.IMAGES_GIFS_WORDS:
        response = requests.get(config.IMAGES_GIFS[msg])
        json_data = json.loads(response.text)
        emb = discord.Embed(title='', colour=discord.Color.blurple())
        emb.set_image(url=json_data['link'])
        await message.channel.send(embed=emb)

    # Обновление информации о канале
    channel = message.guild.get_channel(config.SETTINGS['ALL_MEMBERS_CHANNEL_ID'])
    await channel.edit(name=f'Всего: {message.guild.member_count}')


# Пинг
@BOT.command()
async def ping(ctx, ping_def=50):
    ping_def = ping_def / 1000
    ping = BOT.ws.latency
    ping_emoji_send = ''
    ping_em = ping // ping_def
    un_ping_em = (0.500 // ping_def) - ping_em + 1
    ping_emoji = '🔳'
    if ping < ping_def:
        await ctx.send(content=f"`Пинг? Какой пинг? Пинг меньше {ping_def * 1000:.0f}!`")
    if ping >= ping_def:
        ping_emoji = '🟩'
    if ping >= (0.500 / ping) / 3:
        ping_emoji = '🟧'
    if ping >= ((0.500 / ping) / 3) * 2:
        ping_emoji = '🟥'
    while ping_em > 0:
        ping_emoji_send += ping_emoji
        ping_em = ping_em - 1
    while un_ping_em > 0:
        ping_emoji_send += '🔳'
        un_ping_em = un_ping_em - 1
    if ping > 0.500:
        await ctx.send(content=f'`Бот в ахуе, пинг больше 500`')
    await ctx.send(content=f'`Пинг бота: {ping * 1000:.0f}ms \n {ping_emoji_send}`')


# Мегумин <3
@BOT.command()
async def waifu(ctx):
    emb = discord.Embed(title='Секретная команда!', colour=discord.Color.green())
    emb.add_field(name='Моя вайфу - ', value='[Megumin!](https://konosuba.fandom.com/wiki/Megumin)', inline=True)
    await ctx.send(embed=emb)


# Донат разработчику
@BOT.command()
async def donate(ctx):
    emb = discord.Embed(title='Разработчик бота - KreO', colour=discord.Color.green())
    emb.add_field(name='Связь:', value='Discord - KreO#2883', inline=False)
    emb.add_field(name='Донат на карту:', value='Нету', inline=False)
    emb.add_field(name='Донат алёртом:', value='[Donation Alerts](https://www.donationalerts.com/r/kreo)', inline=False)
    await ctx.send(embed=emb)


# Ссылка на любой сайт
@BOT.command()
async def site(ctx, arg='youtube'):
    if arg == 'p1':
        await ctx.send('https://hentaihaven.com')
    elif arg == 'p2':
        await ctx.send('https://pornhub.com')
    elif arg == 'p3':
        await ctx.send('https://xvIDeos.com')
    else:
        await ctx.send(f'https://{arg}.com')


# Ссылка для приглашения друзей
@BOT.command()
async def link(ctx):
    await ctx.send(config.SETTINGS['LINK'])


# Информация о пользователе
@BOT.command()
async def info(ctx, member: discord.Member):
    emb = discord.Embed(title='Информация о пользователе', colour=discord.Color.dark_gold())
    emb.add_field(name='Когда присоеденился к серверу: ', value=member.joined_at.strftime("%#d, %B, %Y, %I:%M %p"), inline=False)
    emb.add_field(name='Активность: ', value=f'{member.web_status}, {member.activity}', inline=False)
    emb.add_field(name='Бот: ', value=member.bot, inline=False)
    emb.add_field(name='Имя: ', value=f'{member.name}#{member.discriminator}', inline=False)
    emb.add_field(name='Айди: ', value=member.id, inline=False)
    emb.add_field(name='Аккаунт был создан: ', value=member.created_at.strftime("%#d, %B, %Y, %I:%M %p"), inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=emb)


@BOT.command()
async def report(ctx, mem: discord.Member):
    admin_channel = ctx.guild.get_channel(config.SETTINGS['ADMIN_CHANNEL_ID'])
    await admin_channel.send(f'На пользователя [{mem}]({mem.mention}) поступила жалоба.')


# Добавление роли пользователю
@BOT.command()
@commands.has_permissions(administrator=True)
async def give(ctx, member: discord.Member, getrole: discord.Role):
    try:
        role = discord.utils.get(ctx.guild.roles, id=getrole.id)
        await member.add_roles(role)
        print(f'User [{member}] get role [{role}]')
    except Exception:
        await ctx.send(f'Неверное имя пользователя или роль! ({member}, {role})')


# Отнятие роли у пользователя
@BOT.command()
@commands.has_permissions(administrator=True)
async def remove(ctx, member: discord.Member, getrole: discord.Role):
    try:
        role = discord.utils.get(ctx.guild.roles, id=getrole.id)
        await member.remove_roles(role)
        print(f'User: [{member}], removed role: [{role}]')
    except Exception:
        await ctx.send(f'Неверное имя пользователя или роль! (ну или роль слишком крута для меня) ({member}, {getrole})')


# Очистка чата
@BOT.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, AMOUNT=config.SETTINGS['AMOUNT']):
    await ctx.channel.purge(limit=AMOUNT + 1)


# Кик
@BOT.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Кик', colour=discord.Colour.orange())
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Ибо нехуй', value='Кикнутый - {}'.format(member.mention))
    try:
        await member.kick(reason=reason)
        await ctx.send(embed=emb)
        print(f'Kicked {member.mention}')
    except Exception:
        await ctx.send("Кикать админа? Серьёзно?")


# Бан
@BOT.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Бан', colour=discord.Colour.red())
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='В ебало', value='Забаненый - {}'.format(member.mention))
    try:
        await member.ban(reason=reason)
        await ctx.send(embed=emb)
        print(f'Banned {member.mention}')
    except Exception:
        await ctx.send("Банить админа? Серьёзно?")


# Разбан
@BOT.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        emb = discord.Embed(title='Разбан', colour=discord.Colour.blue())
        emb.set_author(name=user.name, icon_url=user.avatar_url)
        emb.add_field(name='Везунчик сука', value='Разбаненый - {}'.format(user.mention))
        await ctx.send(embed=emb)
        print(f'Unbanned {user.mention}')
        return


BOT.run(config.SETTINGS['TOKEN'])
