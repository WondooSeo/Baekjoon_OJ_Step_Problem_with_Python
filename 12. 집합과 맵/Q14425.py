import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    S, ans = set(), 0

    for _ in range(N):
        S.add(sys.stdin.readline().rstrip())
    for _ in range(M):
        if sys.stdin.readline().rstrip() in S:
            ans += 1

    print(ans)
