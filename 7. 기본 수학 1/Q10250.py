import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        H, W, N = map(int, sys.stdin.readline().rstrip().split())
        print(((N-1)%H + 1) * 100 + ((N-1)//H) + 1)
