import sys

if __name__ == '__main__':
    X = int(sys.stdin.readline().rstrip())
    now_count, total_count = 1, 0
    while True:
        total_count += now_count
        if total_count >= X:
            break
        now_count += 1

    bunja = total_count - X + 1
    if now_count%2 == 1:
        print(f'{bunja}/{now_count - bunja + 1}')
    else:
        print(f'{now_count - bunja + 1}/{bunja}')
