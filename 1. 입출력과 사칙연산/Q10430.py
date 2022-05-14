import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)
