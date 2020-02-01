class Analy:
    def __init__(self, name, path, text, hour, minute):
        '''
        :param name, 群聊名称初始化
                path,路径
                text,发送的内容
                hour,小时
                minute,分钟
        '''
        self.name = name
        self.path = path
        self.text = text
        self.hour = hour
        self.minute = minute

    def parser(self):  # 解析输入的参数，对无效参数做处理
        args = {}
        parser = {}
        args['name'] = self.name
        args['pathText'] = self.get_path_text() if self.get_path_text() else None
        args['text'] = self.text if self.text else None
        args['hour'] = self.hour
        args['minute'] = self.minute
        for arg in args:
            if args[arg] is not None:
                parser[arg] = args[arg]
        return parser

    def get_path_text(self):  # 获得文件的内容
        path = self.path
        if path:
            f = open(path, 'r').read()
            return f
        else:
            return None
