from collections import namedtuple
User=namedtuple('User',['name','sex','birth'])
name = namedtuple("name", ["surName", "nickName"])
birth = namedtuple("birth", ["wcalender", "ccalender"])
user1=User._make([name('yty1','yy1'),'male',birth('0908','0726')])
user2=User._make([name('yty2','yy2'),'male',birth('0619','0517')])
user3=User._make([name('yty3','yy3'),'male',birth('0521','0406')])
print('user1大名是:',user1.name.surName,'\n','小名是：',user1.name.nickName,'\n','性别是：',user1.sex,'\n','阳历生日：',user1.birth.wcalender,'\n','阴历生日：',user1.birth.ccalender)
print('user2大名是:',user2.name.surName,'\n','小名是：',user2.name.nickName,'\n','性别是：',user2.sex,'\n','阳历生日：',user2.birth.wcalender,'\n','阴历生日：',user2.birth.ccalender)
print('user3大名是:',user3.name.surName,'\n','小名是：',user3.name.nickName,'\n','性别是：',user3.sex,'\n','阳历生日：',user3.birth.wcalender,'\n','阴历生日：',user3.birth.ccalender)