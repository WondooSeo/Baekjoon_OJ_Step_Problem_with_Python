import sys

def gcd(x, y) -> int:
    while y > 0:
        x, y = y, x%y
    return x

if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A*B//gcd(A, B))
