import sys

if __name__ == '__main__':
    now_year = int(sys.stdin.readline().rstrip())

    if (now_year%4 == 0 and now_year%100) or now_year%400 == 0:
        print(1)
    else:
        print(0)
