from collections import namedtuple

User = namedtuple('User',['name','sex','birth'])

class name:

    def __init__(self,surName,nickName):
        self.surName = surName
        self.nickName = nickName

class birth:

    def __init__(self,wcalendar,ccalendar):
        self.wcalendar = wcalendar
        self.ccalendar = ccalendar

users = [
    (name('罗杨美慧','美慧'),'女',birth('19970820','19970718')),
    (name('张三','three'),'男',birth('19990101','19990101')),
    (name('李四','four'),'男',birth('19990101','19990101'))
]

for user in users:
    user = User._make(user)

    print('大名叫：',user.name.surName)
    print('{}的小名叫：{}'.format(user.name.surName,user.name.nickName))
    print('{}的年龄是：{}'.format(user.name.nickName,user.sex))
    print('{}的阳历生日是：{}'.format(user.name.nickName,user.birth.wcalendar))
    print('{}的阴历生日是：{}'.format(user.name.nickName,user.birth.ccalendar))
