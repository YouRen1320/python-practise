import random

random_num = random.randint(1, 100)

while 1:
    num = int(input('请输入您的数字：'))
    if 0 < num < 100:
        if num < random_num:
            print('你的数字猜小了！')
        elif num > random_num:
            print('你的数字猜大了！')
        else:
            print('恭喜您猜对了！')
            break
    else:
        print('请输入0-100以内的数字！')
