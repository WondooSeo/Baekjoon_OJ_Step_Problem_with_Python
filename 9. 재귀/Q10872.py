import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print(factorial(N))
