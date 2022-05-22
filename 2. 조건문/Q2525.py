import sys

if __name__ == '__main__':
    A, B = map(int, sys.stdin.readline().rstrip().split())
    C = int(sys.stdin.readline().rstrip())

    cook_hour, cook_min = C//60, C%60
    A += cook_hour
    B += cook_min
    if B >= 60:
        A += B//60
        B = B%60
    if A >= 24:
        A -= 24

    print(A, B)
