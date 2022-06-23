import sys
from math import ceil

if __name__ == '__main__':
    A, B, V = map(int, sys.stdin.readline().rstrip().split())
    now_days = ceil((V-A)/(A-B)) + 1
    print(now_days)
