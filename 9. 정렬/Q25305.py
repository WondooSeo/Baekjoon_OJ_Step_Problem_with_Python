import sys

if __name__ == '__main__':
    N, k = map(int, sys.stdin.readline().rstrip().split())
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    x.sort(reverse=True)
    print(x[k-1])
