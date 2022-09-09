import sys

def hanoi(n, start, rem, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, rem)
        print(start, end)
        hanoi(n-1, rem, start, end)

if __name__ == '__main__':
    K = int(sys.stdin.readline().rstrip())
    print(2**K-1)
    hanoi(K, 1, 2, 3)
