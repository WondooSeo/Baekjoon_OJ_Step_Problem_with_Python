import sys

def gcd(a, b) -> int:
    while b > 0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    now_gcd = gcd(n, m)
    print(now_gcd, n*m//now_gcd, sep='\n')
