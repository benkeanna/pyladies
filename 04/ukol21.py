for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print('bum-bác')
    elif i % 5 == 0:
        print('bác')
    elif i % 3 == 0 :
        print('bum')
    else:
        print(i)
