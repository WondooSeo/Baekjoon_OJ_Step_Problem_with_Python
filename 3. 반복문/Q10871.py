import sys

if __name__ == '__main__':
    N, X = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    for num in A:
        if num < X:
            print(num, end=' ')
