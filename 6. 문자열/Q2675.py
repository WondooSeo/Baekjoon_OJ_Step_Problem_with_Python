import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        R, S = sys.stdin.readline().rstrip().split()
        R = int(R)
        for now_chr in S:
            print(now_chr*R, end='')
        print()