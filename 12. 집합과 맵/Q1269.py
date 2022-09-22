import sys

if __name__ == '__main__':
    nA, nB = map(int, sys.stdin.readline().rstrip().split())
    A = set(map(int, sys.stdin.readline().rstrip().split()))
    B = set(map(int, sys.stdin.readline().rstrip().split()))
    print(len(A.union(B))-len(A.intersection(B)))
