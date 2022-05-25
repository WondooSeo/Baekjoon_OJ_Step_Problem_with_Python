import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    ans = 0

    for i in range(n):
        ans += i + 1

    print(ans)
