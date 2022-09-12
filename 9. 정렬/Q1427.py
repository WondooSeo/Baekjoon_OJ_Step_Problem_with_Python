import sys

if __name__ == '__main__':
    N = list(map(int, sys.stdin.readline().rstrip()))
    N.sort(reverse=True)
    print(*N, sep='')
