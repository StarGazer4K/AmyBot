from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio
from aiocqhttp.message import MessageSegment
import random
import os

__plugin_name__ = '本地图'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

@on_command('色图',aliases=('色图','涩图','色色','涩涩','色','涩'))
async def _(session: CommandSession):
    num = int(session.ctx['group_id'])
    ran = random.randint(1,789)
    url = "sese/" + str(ran) + ".png"
    if num == 123 or num == 456:#mczoo&ark
        #await session.send('本群不支持涩图功能~')
        pass
    else :
        await session.send(MessageSegment.image(url))
        
@on_command('玫兰莎语录',aliases=('玫兰莎语录','玫兰莎','玫兰莎语','mls','玫兰','玫','兰','莎'))
async def _(session: CommandSession):
    num = int(session.ctx['group_id'])
    ran = random.randint(1,243)
    url = "miao/" + str(ran) + ".png"
    if num == 123:
        pass
    else :
        await session.send(MessageSegment.image(url))
        
@on_command('内鬼语录',aliases=('内鬼语录','内鬼','内鬼语'))
async def _(session: CommandSession):
    num = int(session.ctx['group_id'])
    ran = random.randint(1,62)
    file_name = os.listdir("/home/pi/AmyBot/else/data/images/mczoo")
    url = "mczoo/" + str(file_name[ran])
    if num == 456:#ark
        pass
    else :
        await session.send(MessageSegment.image(url))