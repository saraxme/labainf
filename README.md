# labainf
while True:
    try:
        A = float(input('Введите число больше 1: '))
        if A > 1:
            break
    except ValueError:
        print('Это не число')

summ = 0
for k in range(1, 10**6):
    summ += 1/k
    #print(summ)
while summ > A:
    print(k, summ)
    break
