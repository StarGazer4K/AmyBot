from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio
import json

__plugin_name__ = '肥啾'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

@on_command('肥啾')
async def _(session: CommandSession):
    async with aiohttp.request("GET","http://api.bilibili.com/x/relation/stat?vmid=698018684")as resp:
        json_str=await resp.text()
    json_str=str(json_str)
    if resp.status != 200:
        await session.send('网络错误')
    else:
        doc = json.loads(json_str)
        following = doc['data']['following']
        follower = doc['data']['follower']
        res = "肥啾关注了" + str(following) + "人，有" + str(follower) + "个粉丝w~"
        await session.send(res)