# WeiXinSendMsg
============================  
目前有两个功能  
一个是直接发送消息  
另外一个是定时发送消息  
============================  
  
============================  
  
需要itchat库和apscheduler库  
可以使用  
pip install itchat  
pip install apscheduler  
来安装  
=============================  
使用的时候用  
python main.py -h 查看帮助信息  
帮助信息：   
positional arguments:  
  g                     要发送消息的群聊名称  
  
optional arguments:  
  -h, --help            show this help message and exit   
  --text TEXT, -t TEXT  要发送的内容，使用-f/--file可以从文件里读取    
  --file FILE, -f FILE  从文件读取要发送的内容，文件路径    
  --hour HOUR           发送消息的时间，小时[0-23]    
  --minute MINUTE, -m MINUTE   
                        发送的分钟，默认0  
  --flag FLAG           [0-1]请选择模式，默认0为定时发送，1为直接发送消息  
  
g参数为必须参数,  
Exmple  
 python main.py 电子17级2班班级群 -t 安全 -h 0 -m 0 --flag 0  
 这是每天0点0分定时向 电子17级2班班级群 发送 安全  
 
-f/--file 为从文件读取发送的内容，可以再main.py文件目录新建一个txt向其中写入要发送的内容，然后使用此参数,-f [path]  
============================  
