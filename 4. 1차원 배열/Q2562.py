import sys

if __name__ == '__main__':
    max_num, max_index = -1, 0
    for i in range(9):
        now_num = int(sys.stdin.readline().rstrip())
        if now_num > max_num:
            max_num = now_num
            max_index = i+1

    print(max_num, max_index, sep='\n')
