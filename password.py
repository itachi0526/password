x = 3
while x > 0:
    password = input('請輸入密碼： ')
    if password == 'fbiopenthedoor':
        print('麥當勞歡樂送！！！')
        break
    else:
        x = x - 1
        print('笑死，熊頭你只剩下', x,'次機會')
        if x == 0: #
            break           