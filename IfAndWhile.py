import random
# -*- coding utf-8 -*-

guess = int(input('请输入一个数字'))
secret = random.randint(1,10)
counts = 0
while guess != secret:
    counts=counts+1
    if counts<3:
        
        if guess==secret:
            print('OK')
        else:
            if guess < secret:
                print('小了')
                temp = input("猜错了请重新输入")
                guess =int(temp)
            else:
                print('大了')
                temp = input("猜错了请重新输入")
                guess =int(temp)
    else:
        print('超过次数')
        break
print('猜对了，循环结束')
        