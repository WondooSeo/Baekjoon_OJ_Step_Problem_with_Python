import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    # Using for loop
    # for i in range(N, 0 , -1):
    #     print(i)

    # Using range & list
    now_list = list(range(N, 0, -1))
    print(*now_list, sep='\n')
