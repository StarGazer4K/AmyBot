from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
import aiohttp
import asyncio
import json
import random

__plugin_name__ = '在线'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

@on_command('在线111111')
async def _(session: CommandSession):
    if int(session.ctx['user_id']) == 22313112312313123213143432:
        async with aiohttp.request(
                "GET", "https://api.lolicon.app/setu/v2"
        ) as resp:
            json_str = await resp.text()
        doc = json.loads(json_str)
        url = doc['data'][0]['urls']['original']
        await session.send(MessageSegment.image(url))

@on_command('猫猫图',aliases=('猫','猫猫','猫图'))
async def _(session: CommandSession):
    async with aiohttp.request(
            "GET", "https://api.thecatapi.com/v1/images/search"
    ) as resp:
        json_str = await resp.text()
    if resp.status != 200:
        await session.send('网络错误')
    else:
        doc = json.loads(json_str)
        url = doc[0]['url']
        await session.send(MessageSegment.image(url))

@on_command('狗狗图',aliases=('狗','狗狗','狗图'))
async def _(session: CommandSession):
    async with aiohttp.request(
            "GET", "https://dog.ceo/api/breeds/image/random"
    ) as resp:
        json_str = await resp.text()
    if resp.status != 200:
        await session.send('网络错误')
    else:
        doc = json.loads(json_str)
        url = doc['message']
        await session.send(MessageSegment.image(url))
    
@on_command('狐狸图',aliases=('狐','狸','狐狸','狐狸图'))
async def _(session: CommandSession):
    random_num = random.randint(1, 123)
    str_fox = "https://randomfox.ca/images/" + str(random_num) + ".jpg"
    await session.send(MessageSegment.image(str_fox))
