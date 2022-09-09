import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list()
    for _ in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    # Insert sort
    # for i in range(1, N):
    #     for j in range(i, 0, -1):
    #         if num_list[j-1] > num_list[j]:
    #             num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

    # for num in num_list:
    #     print(num)

    # Bubble sort
    for i in range(N-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    for num in num_list:
        print(num)
