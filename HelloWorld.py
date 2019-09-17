X!上班好累！
# -*- coding: UTF-8 -*-

import datetime

x = datetime.datetime.now()  # 現在時間

h = 16 - x.hour
m = 60 - x.minute

if (x.minute == 60):
    h = h + 1

print ('還有 %s時 %s分就可以下班啦！！'%(h, m))
print ('如果晚點來的自己家時間阿！！ ')
