import sys

if __name__ == '__main__':
    member_list = list()
    for N in range(int(sys.stdin.readline().rstrip())):
        now_age, now_name = sys.stdin.readline().rstrip().split()
        member_list.append([int(now_age), now_name])

    member_list.sort(key=lambda x: (x[0]))
    for now_member in member_list:
        print(*now_member)
