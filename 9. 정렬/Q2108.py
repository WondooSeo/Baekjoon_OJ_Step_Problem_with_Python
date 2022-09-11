import sys
from collections import Counter

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list()
    for _ in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))
    num_list.sort()

    # 1. Arithmatic mean
    if sum(num_list) >= 0:
        print(int(sum(num_list)/N + 0.5))
    else:
        print(int(sum(num_list)/N - 0.5))

    # 2. Median
    print(num_list[N//2])

    # 3. Mode
    if N == 1:
        print(num_list[0])
    else:
        now_mode = Counter(num_list).most_common(2)
        if now_mode[0][1] == now_mode[1][1]:
            print(now_mode[1][0])
        else:
            print(now_mode[0][0])

    # 4. Range
    print(max(num_list) - min(num_list))
