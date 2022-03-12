from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
import aiohttp
import asyncio

__plugin_name__ = '鸡汤'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

async def get_text(num:int):
    url = "https://api.oddfar.com/yl/q.php?c=" + str(num) + "&encode=text"
    async with aiohttp.request("GET",url)as resp:
        json_str=await resp.text()
    json_str=str(json_str)
    if resp.status != 200:
        return '网络错误'
    else:
        return json_str

@on_command('鸡汤')
async def _(session: CommandSession):
    async with aiohttp.request("GET","http://api.btstu.cn/yan/api.php")as resp:
        json_str=await resp.text()
    json_str=str(json_str)
    if resp.status != 200:
        await session.send('网络错误')
    else:
        await session.send(json_str)
        
@on_command('土味情话')
async def _(session: CommandSession):
    temp = await get_text(1001)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('精神语录')
async def _(session: CommandSession):
    temp = await get_text(1002)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)
        
@on_command('网易云热评')
async def _(session: CommandSession):
    temp = await get_text(1003)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)
        
@on_command('成人笑话')
async def _(session: CommandSession):
    temp = await get_text(1004)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('奇葩对话')
async def _(session: CommandSession):
    temp = await get_text(1005)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('舔狗日记')
async def _(session: CommandSession):
    temp = await get_text(1006)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('毒鸡汤')
async def _(session: CommandSession):
    temp = await get_text(1007)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('朋友圈文案')
async def _(session: CommandSession):
    temp = await get_text(1008)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('骂人宝典')
async def _(session: CommandSession):
    temp = await get_text(1009)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('动画')
async def _(session: CommandSession):
    temp = await get_text(2001)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('漫画')
async def _(session: CommandSession):
    temp = await get_text(2002)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('游戏')
async def _(session: CommandSession):
    temp = await get_text(2003)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('文学')
async def _(session: CommandSession):
    temp = await get_text(2004)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('原创')
async def _(session: CommandSession):
    temp = await get_text(2005)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('来自网络')
async def _(session: CommandSession):
    temp = await get_text(2006)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('其他')
async def _(session: CommandSession):
    temp = await get_text(2007)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('影视')
async def _(session: CommandSession):
    temp = await get_text(2008)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('诗词')
async def _(session: CommandSession):
    temp = await get_text(2009)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('网易云')
async def _(session: CommandSession):
    temp = await get_text(2010)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('哲学')
async def _(session: CommandSession):
    temp = await get_text(2011)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('抖机灵')
async def _(session: CommandSession):
    temp = await get_text(2012)
    if temp == '网络错误':
        await session.send('网络错误')
    else:
        await session.send(temp)

@on_command('t')
async def _(session: CommandSession):
    await session.send(MessageSegment.poke('type_',str(session.ctx['user_id'])))
    print(int(session.ctx['user_id']))

@on_command('a')
async def _(session: CommandSession):
    await session.send(MessageSegment.at(str(session.ctx['user_id'])))
    print(int(session.ctx['user_id']))

@on_command('tt')
async def _(session: CommandSession):
    msg = MessageSegment.at(str(session.ctx['user_id'])) + MessageSegment.text(str(session.ctx['user_id']))
    await session.send(msg)
    #print(int(session.ctx['user_id']))




