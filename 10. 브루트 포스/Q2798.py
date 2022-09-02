import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    card = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = -1

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                now_card = card[i] + card[j] + card[k]
                if ans < now_card <= M:
                    ans = now_card

    print(ans)
