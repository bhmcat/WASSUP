# coffee.py
coffee = 10
while True:
    money = int(input('돈을 넣어라: '))
    if money == 300:
        print('커피준다')
        coffee -= 1
        print(f'남은커피 {coffee}남았다')
    elif money > 300:
        print(f'잔돈 {money}준다 커피도 준다')
        coffee -= 1
        print(f'남은커피 {coffee}남았다')
    else:
        print('돈 가져가라. 커피 안준다')
        print(f'남은커피 {coffee}남았다')
    if coffee == 0:
        print('남은커피 없다. 커피 안판다')
        break