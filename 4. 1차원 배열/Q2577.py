import sys

if __name__ == '__main__' :
    A = int(sys.stdin.readline().rstrip())
    B = int(sys.stdin.readline().rstrip())
    C = int(sys.stdin.readline().rstrip())
    ABC = list(map(int, str(A*B*C)))
    count_list = [0 for _ in range(10)]

    for now_ABC in ABC:
        count_list[now_ABC] += 1

    print(*count_list, sep='\n')
