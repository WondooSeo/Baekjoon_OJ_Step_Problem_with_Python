import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for _ in range(N):
        now_str = sys.stdin.readline().rstrip()
        is_group = True
        for i in range(len(now_str)-1):
            if now_str[i] == now_str[i+1]:
                continue
            else:
                if now_str[i] in now_str[i+1:]:
                    is_group = False
                    break

        if is_group:
            count += 1

    print(count)
    