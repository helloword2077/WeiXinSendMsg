import itchat
import datetime
import argparse
from tools.tools import Tools
from tools.analysis import Analy


# ======================命令行参数设置=======================

parser = argparse.ArgumentParser()
parser.add_argument('g', type=str, help='要发送消息的群聊名称')
parser.add_argument('--text', '-t', type=str, help='要发送的内容，使用-f/--file可以从文件里读取')
parser.add_argument('--file', '-f', type=str, help='从文件读取要发送的内容，文件路径')
parser.add_argument('--hour', type=int, default=0, help='发送消息的时间，小时[0-23]')
parser.add_argument('--minute', '-m', type=int, default=0, help='发送的分钟，默认0')
parser.add_argument('--flag', type=int, default=0, help='[0-1]请选择模式，默认0为定时发送，1为直接发送消息')

args = parser.parse_args()

# ============================解析============================

NAME = args.g
PATH = args.file

HOUR = args.hour
MINUTE = args.minute
FLAG = args.flag
te = args.text

arg = Analy(NAME, PATH, te, HOUR, MINUTE).parser()
arg['text'] = None if 'text' not in arg else arg['text']
text = arg['text'] if arg['text'] else arg['pathText']  # 读取函数的text和从文件获得的pathText
hour = arg['hour']  # 读取hour
minute = arg['minute']  # 读取minute

# ===========================================================


itchat.auto_login(hotReload=True)
print('=======登录成功========')
fun = Tools(NAME, text, hour, minute)

# ===========================================================


if FLAG == 1:
    fun.send_msg()  # 直接发送消息函数
else:
    fun.timing()

# ======================YM=20201.31=============================
