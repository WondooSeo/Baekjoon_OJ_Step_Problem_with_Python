import sys

def is_hansu(n):
    now_n = list(map(int, str(n)))
    if len(now_n) == 1:
        return True
    else:
        now_diff = now_n[1] - now_n[0]
        for i in range(1, len(now_n)-1):
            if now_n[i+1] - now_n[i] != now_diff:
                return False
        return True


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for j in range(1, N+1):
        if is_hansu(j):
            count += 1

    print(count)
