import sys

if __name__ == '__main__':
    x_list, y_list = list(), list()
    for _ in range(3):
        now_x, now_y = map(int, sys.stdin.readline().rstrip().split())
        x_list.append(now_x)
        y_list.append(now_y)

    print(2*sum(set(x_list))-sum(x_list), 2*sum(set(y_list))-sum(y_list))
