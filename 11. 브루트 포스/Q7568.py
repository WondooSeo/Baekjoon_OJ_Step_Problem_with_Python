import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    dungchi, score = list(), [1 for _ in range(N)]
    for _ in range(N):
        dungchi.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for i in range(N):
        for j in range(N):
            if i != j and dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
                score[i] += 1

    print(*score)
