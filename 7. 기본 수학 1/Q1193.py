import sys

if __name__ == '__main__':
    X = int(sys.stdin.readline().rstrip())
    now_count, temp = 1, 0
    while True:
        temp += now_count
        if temp >= X:
            break
        now_count += 1

