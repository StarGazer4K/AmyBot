from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio

__plugin_name__ = '抽卡'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

@on_command('十连')
async def _(session: CommandSession):
    num = int(session.ctx['group_id'])
    common_order = '十连结果如下:\n'
    special_order = '玫兰莎'
    await session.send(common_order+special_order)
    
@on_command('单抽')
async def _(session: CommandSession):
    common_order = '单抽结果如下:\n'
    special_order = '玫兰莎'
    await session.send(common_order+special_order)
