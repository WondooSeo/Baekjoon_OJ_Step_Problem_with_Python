import sys

def bt():
    global N, M
    if len(bt_list) == M:
        print(*bt_list)
        return

    for i in range(1, N+1):
        if len(bt_list) == 0 or bt_list[-1] < i:
            bt_list.append(i)
            bt()
            bt_list.pop()

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    bt_list = list()
    bt()
