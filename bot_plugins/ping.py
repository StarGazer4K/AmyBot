from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('ping')
async def _(session: CommandSession):
    await session.send('pong!')
    
@on_command('rbq',aliases=('rbq','RBQ'))
async def _(session: CommandSession):
    await session.send('嘤嘤嘤,人家不想做RBQ啦')