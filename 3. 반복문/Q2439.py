import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    for i in range(N):
        print(' '*(N-i-1) + '*'*(i+1))
