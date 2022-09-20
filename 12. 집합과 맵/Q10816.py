import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_card = list(map(int, sys.stdin.readline().rstrip().split()))
    num_dict = dict()
    for now_card in num_card:
        if now_card in num_dict:
            num_dict[now_card] += 1
        else:
            num_dict[now_card] = 1

    M = int(sys.stdin.readline().rstrip())
    s_card = list(map(int, sys.stdin.readline().rstrip().split()))
    for now_card in s_card:
        if now_card in num_dict:
            print(num_dict[now_card], end=' ')
        else:
            print(0, end=' ')
