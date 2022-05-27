import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    # Using for loop
    # for i in range(N):
    #     print(i + 1)

    # Using range & list
    now_list = list(range(1, N+1))
    print(*now_list, sep='\n')
