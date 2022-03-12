from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio
from aiocqhttp.message import MessageSegment
import os

@on_command('tpic',permission = lambda sender:sender.is_superuser)
async def _(session: CommandSession):
    file_name = os.listdir("/home/pi/AmyBot/else/data/images/temp")
    url = "temp/" + str(file_name[0])
    await session.send(MessageSegment.image(url))

@on_command('ttxt',permission = lambda sender:sender.is_superuser)
async def _(session: CommandSession):
    f = open('/home/pi/AmyBot/else/data/images/temp/temp.txt','r')
    str_txt = f.read()
    f.close()
    await session.send(str_txt)
    
@on_command('ttpic',permission = lambda sender:sender.is_superuser)
async def _(session: CommandSession):
    bot = nonebot.get_bot()
    msg = [
        {
            'type':'image',
            'data':'https://img04.sogoucdn.com/app/a/200692/621_2660_feedback_232d041732cd47b2974f84c1efcabaae.png'
        }
    ]
    await bot.send_group_msg(group_id = 123,message = msg)