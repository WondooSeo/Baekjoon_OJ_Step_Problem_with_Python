import sys

def bt():
    global N, M
    if len(comb) == M:
        print(*comb)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        comb.append(i)
        bt()
        comb.pop()
        visited[i] = False

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    comb = list()
    visited = [False for _ in range(N+1)]
    bt()
