import sys

def div_sum(n) -> int:
    count = 1
    while count <= 1000000:
        now_sum = count + sum(map(int, list(str(count))))
        if now_sum == n:
            return count
        count += 1
    return 0

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print(div_sum(N))
