while True:
    try:
        N = int(input('Введите число больше 0: '))
        if N > 0:
            break
    except ValueError:
        print('Это не число')
N2 = 0
for k in range(1, N + 1):
    N2 += 2*k-1
    print(N2)