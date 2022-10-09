import sys

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(factorial(N)//(factorial(K)*factorial(N-K)))
