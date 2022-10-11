import sys

def combination(a, b):
    bunja, bunmo = 1, 1
    for i in range(b-a+1, b+1):
        bunja *= i
    for i in range(1, a+1):
        bunmo *= i

    return bunja//bunmo

if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        print(combination(N, M))
