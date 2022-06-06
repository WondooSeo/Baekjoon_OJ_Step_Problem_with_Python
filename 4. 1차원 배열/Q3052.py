import sys

if __name__ == '__main__':
    remain_list = list()

    for _ in range(10):
        now_remain = int(sys.stdin.readline().rstrip()) % 42
        if now_remain not in remain_list:
            remain_list.append(now_remain)

    print(len(remain_list))
