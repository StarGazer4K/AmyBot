from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio

__plugin_name__ = '指令'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

common_order = '通用指令:新闻,狗狗图,狐狸图,猫猫图,土味情话,精神语录,网易云热评,成人笑话,奇葩对话,舔狗日记,毒鸡汤,鸡汤,朋友圈文案,骂人宝典,动画,漫画,游戏,文学,原创,来自网络,其他,影视,诗词,网易云,哲学,抖机灵\n'

@on_command('指令',aliases=('指令','查询','帮助','命令','菜单'))
async def _(session: CommandSession):
    num = int(session.ctx['group_id'])
    special_order = '专用指令:'
    if num == 123:#mczoo
        special_order += '服务器,肥啾,内鬼语录'
        await session.send(common_order+special_order)
    elif num == 456:#arknights
        special_order += '玫兰莎语录'#,涩图
        await session.send(common_order+special_order)
    else :
        await session.send(common_order)