from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
from aiocqhttp.exceptions import Error as CQHttpError
import nonebot
import aiohttp
import asyncio
import json#http://api.tianapi.com/healthtip/index?key=AP

__plugin_name__ = '新闻'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

async def get_wanan():
    async with aiohttp.request(
            "GET", "http://api.tianapi.com/wanan/index?key="#需要去天行数据自行申请key
    ) as resp:
        json_str = await resp.text()
    if resp.status != 200:
        return 'err'
    else:
        doc = json.loads(json_str)
        dic = str(doc['newslist'][0]['content'])
        return dic

@on_command('晚安',permission = lambda sender:sender.is_superuser)
async def _(session: CommandSession):
    temp = await get_wanan()
    if temp == 'err':
        await session.send('网络错误')
    else:
        await session.send(temp)
        
@nonebot.scheduler.scheduled_job('cron',hour='22',minute='25')
async def _1():
    bot = nonebot.get_bot()
    msg1 = '各位晚上好~\n'
    msg2 = '玫兰莎'
    msg3 = '托我给大家送上晚安心语:\n'
    msg4 = await get_wanan()
    msg5 = '喵~~~'
    msg = msg1 + msg2 + msg3 + msg4 + msg5
    try:
        await bot.send_group_msg(group_id = 123,message = msg)
    except CQHttpError:
        pass

@nonebot.scheduler.scheduled_job('cron',hour='22',minute='30')
async def _1():
    bot = nonebot.get_bot()
    msg1 = '各位晚上好~\n'
    msg2 = 'xm'
    msg3 = '托我给大家送上晚安心语:\n'
    msg4 = await get_wanan()
    msg5 = '喵~~~'
    msg = msg1 + msg2 + msg3 + msg4 + msg5
    try:
        await bot.send_group_msg(group_id = 456,message = msg)
    except CQHttpError:
        pass
