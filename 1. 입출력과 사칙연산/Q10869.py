import sys

if __name__ == '__main__':
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B, A-B, A*B, A//B, A%B, sep='\n')
