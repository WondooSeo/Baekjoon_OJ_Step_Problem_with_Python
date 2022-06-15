import sys

if __name__ == '__main__':
    A, B = sys.stdin.readline().rstrip().split()
    A, B = list(A), list(B)
    A.reverse()
    B.reverse()
    A, B = int(''.join(A)), int(''.join(B))

    print(A) if A > B else print(B)
