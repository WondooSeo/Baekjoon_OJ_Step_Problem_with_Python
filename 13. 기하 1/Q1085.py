import sys

if __name__ == '__main__':
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
    print(min(x, y, w-x, h-y))
