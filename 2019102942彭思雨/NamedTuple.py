from collections import namedtuple
User = namedtuple('User', ['Name', 'Sex', 'Birth'])
Name = namedtuple('Name', ['surName', 'nickName'])
Birth = namedtuple('Birth', ['Lunar_calendar', 'Solar_calendar'])

allUsers = ([Name('贾玲','贾小胖'),'女',Birth('4/27','3/12')],
            [Name('华晨宇','花花'),'男',Birth('3/19','1/27')],
            [Name('于震','大长脸'),'男',Birth('5/17','4/2')],
            [Name('机器猫','蓝胖子'),'男',Birth('10/1','9/5')]
            )

for user in allUsers:
    user = User._make(user)
    #print(user)
    print('大名：'+user.Name.surName+'\t'+'小名：'+user.Name.nickName+
          '\t'+'性别：'+user.Sex+'\t'+'阳历生日：'+user.Birth.Solar_calendar+
          '\t'+'阴历生日：'+user.Birth.Lunar_calendar)







