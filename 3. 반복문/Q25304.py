import sys

if __name__ == '__main__':
    X = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    cost = 0
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        cost += a*b

    print('Yes' if cost == X else 'No')
