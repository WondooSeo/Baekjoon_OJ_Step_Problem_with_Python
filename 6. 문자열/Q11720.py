import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip()))
    print(sum(A))
