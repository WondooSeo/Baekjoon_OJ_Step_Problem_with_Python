import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    chess = list()
    for _ in range(N):
        chess.append(list(sys.stdin.readline().rstrip()))

    min_square = 65
    for i in range(N-7):
        for j in range(M-7):
            W_first, B_first = 0, 0
            for k in range(8):
                for l in range(8):
                    if (k+l)%2 == 0:
                        if chess[i+k][j+l] == 'B':
                            W_first += 1
                        else:
                            B_first += 1
                    else:
                        if chess[i+k][j+l] == 'W':
                            W_first += 1
                        else:
                            B_first += 1

            min_square = min(min_square, W_first, B_first)

    print(min_square)
