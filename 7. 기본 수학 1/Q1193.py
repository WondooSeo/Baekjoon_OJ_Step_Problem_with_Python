import sys

if __name__ == '__main__':
    X = int(sys.stdin.readline().rstrip())
    now_count, total_count = 1, 0
    while True:
        total_count += now_count
        if total_count >= X:
            break
        now_count += 1

    fraction1 = total_count - X + 1
    fraction2 = now_count - fraction1 + 1

    if now_count%2 == 1:
        print(f'{fraction1}/{fraction2}')
    else:
        print(f'{fraction2}/{fraction1}')
