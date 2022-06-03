import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    temp_N = N
    count = 0

    while True:
        temp_N = (temp_N%10)*10 + sum(list(map(int, str(temp_N))))%10
        count += 1
        if temp_N == N:
            break

    print(count)
