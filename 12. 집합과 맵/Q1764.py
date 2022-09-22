import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    DM, BM = set(), set()
    for _ in range(N):
        DM.add(sys.stdin.readline().rstrip())
    for _ in range(M):
        BM.add(sys.stdin.readline().rstrip())
    DBJ = sorted(list(DM.intersection(BM)))
    print(len(DBJ))
    print(*DBJ, sep='\n')
