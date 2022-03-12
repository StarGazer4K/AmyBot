from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_notice,NoticeSession
from aiocqhttp.message import MessageSegment
import nonebot
import aiohttp
import asyncio

__plugin_name__ = '欢迎'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

@on_notice('group_increase')
async def _(session:NoticeSession):
    if session.event.group_id == 722040415:
        bot = nonebot.get_bot()
        Image_url = 'bmd.png'
        msg = MessageSegment.text('欢迎欢迎') + MessageSegment.at(str(session.ctx['user_id'])) + MessageSegment.image(Image_url)
        await bot.send_group_msg(group_id = 123,message = msg)



