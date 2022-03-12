from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
from aiocqhttp.exceptions import Error as CQHttpError
import nonebot
import aiohttp
import asyncio
import json

__plugin_name__ = '新闻'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

async def get_news():
    async with aiohttp.request(
            "GET", "http://api.2xb.cn/zaob"
    ) as resp:
        json_str = await resp.text()
    if resp.status != 200:
        return 'err'
    else:
        dic = {}
        doc = json.loads(json_str)
        Image_url = str(doc['imageUrl'])
        datatime = str(doc['datatime'])
        dic['imageUrl'] = Image_url
        dic['datatime'] = datatime
        return dic

@on_command('新闻')
async def _(session: CommandSession):
    temp = await get_news()
    if temp == 'err':
        await session.send('网络错误')
    else:
        Image_url = temp['imageUrl']
        datatime = temp['datatime']
        await session.send(datatime)
        await session.send(MessageSegment.image(Image_url))

@nonebot.scheduler.scheduled_job('cron',hour='7',minute='30')
async def _1():
    temp = await get_news()
    bot = nonebot.get_bot()
    if temp != 'err':
        Image_url = str(temp['imageUrl'])
        datatime = str(temp['datatime'])
        msg = [
            {
                'type':'image',
                'data':{'file':Image_url}
            }
        ]
        try:
            await bot.send_group_msg(group_id = 123,message = datatime)
            await bot.send_group_msg(group_id = 123,message = msg)
            await bot.send_group_msg(group_id = 456,message = datatime)
            await bot.send_group_msg(group_id = 456,message = msg)
            await bot.send_private_msg(user_id = 789,message = datatime)
            await bot.send_private_msg(user_id = 789,message = msg)
        except CQHttpError:
            pass