import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    print(-1) if C-B <= 0 else print(A//(C-B)+1)
