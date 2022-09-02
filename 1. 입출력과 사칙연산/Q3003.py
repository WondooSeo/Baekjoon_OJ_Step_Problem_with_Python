import sys

if __name__ == '__main__':
    chess_W = list(map(int, sys.stdin.readline().rstrip().split()))
    chess_S = [1, 1, 2, 2, 2, 8]
    for now_S, now_W in zip(chess_S, chess_W):
        print(now_S - now_W, end=' ')
