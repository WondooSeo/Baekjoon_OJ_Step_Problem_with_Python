import sys

def fib(N) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N-1) + fib(N-2)

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    print(fib(n))
