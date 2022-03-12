from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp.message import MessageSegment
from aiocqhttp.exceptions import Error as CQHttpError
import nonebot
import aiohttp
import asyncio
import json

__plugin_name__ = '服务器'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


async def get_mczoo():
    async with aiohttp.request("GET","https://api.miri.site/mcPlayer/get.php?ip=bm.lafamc.com&port=996")as resp:
        json_str=await resp.text()
    json_str=str(json_str)
    if resp.status != 200:
        return '网络错误'
    elif json_str == 'null':
        return "未能获取,请稍后再试"
    else:
        doc = json.loads(json_str)
        # print(f"doc:{doc}")
        online = doc['online']
        player_list = {}
        final_list = ""
        if online != 0:
            for i in range(0, online):
                player_list[i] = doc['sample'][i]['name']
                final_list += str(player_list[i])
                if i != online:
                    final_list += "\n"
            #print("player", i + 1, ":", player_list[i])
            #final_list = final_list[:-2]
            message_zoo = "在线人数：" + str(online) + "\n" + final_list + "TPS<=20.0(内鬼担保)"
            return message_zoo
        else:
            return "服务器空荡荡的"

@on_command('服务器')
async def _(session: CommandSession):
    msg = await get_mczoo()
    bot = nonebot.get_bot()
    await bot.send_group_msg(group_id = 123,message = msg)

@nonebot.scheduler.scheduled_job('cron',hour='*')
async def _1():
    msg = await get_mczoo()
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id = 123,message = msg)
    except CQHttpError:
        pass