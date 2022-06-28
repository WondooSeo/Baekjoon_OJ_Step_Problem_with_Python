import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    sugar_bag = 0
    while N > 0:
        if N % 5 == 0:
            kilo_5 = N//5
            N -= kilo_5*5
            sugar_bag += kilo_5
        else:
            N -= 3
            sugar_bag += 1

    print(-1 if N != 0 else sugar_bag)
