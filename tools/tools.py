import itchat
from datetime import datetime


class Tools:

    def __init__(self, roomname, text, hour, minute):
        self.chatroom = roomname  # 要发送群聊的名字
        self.text = 'test'
        self.hour = hour
        self.minute = minute

    # =================================================================

    def chatrooms(self):
        """
        获取微信中所有群聊的名称
        搜索目标群聊
        获取群聊的name
        :param chatrooms:群聊名称
        :return:目标群聊的UserName信息
        """
        chatroom = self.chatroom  # 获取群聊名
        itchat.get_chatrooms(update=True)  # 获取微信所有群聊信息
        rooms = itchat.search_chatrooms(chatroom)  # 根据名称搜索
        if len(rooms) <= 0:  # 如果没有搜索到
            return None
        else:  # 搜索到了
            return rooms[0]['UserName']

    # =================================================================

    def send_msg(self):
        """

        :param text: 需要输入自定义发送消息
        :return:
        """
        text = '1.黄世鹏 一切正常 从未去过武汉及湖北地区，没有亲戚从武汉及湖北地区来'
        name = self.chatrooms()
        if name is None:
            print('[-]错误，没有找到群聊')
        else:
            print('[+]成功获取群聊信息')
            itchat.send(text, toUserName=name)
            print('[+]成功发送消息,{}'.format(datetime.today())+':'+text)

    # ===========================================================

    def timing(self):
        while True:
            now = datetime.now()
            now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
            time = str(self.hour) + ':' + str(self.minute) + ':' + '00'
            print('\r现在时间：{now},预计发送时间{time},预计发送内容:{text}'.format(now=now_str, time=time, text=self.text), end='')
            if now_str in [time]:
                self.send_msg()
