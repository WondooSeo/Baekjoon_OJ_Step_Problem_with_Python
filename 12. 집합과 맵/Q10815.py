import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_card = set(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    sk_num_card = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = list()

    for now_sk_num_card in sk_num_card:
        if now_sk_num_card in num_card:
            ans.append(1)
        else:
            ans.append(0)

    print(*ans)
