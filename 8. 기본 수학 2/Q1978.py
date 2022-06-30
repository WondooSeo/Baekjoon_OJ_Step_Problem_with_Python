import sys

def prime_sleve() -> list:
    now_sleve = [1 for _ in range(1001)]
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(1000**0.5)+1):
        if now_sleve[i] == 1:
            temp = i * 2
            while temp <= 1000:
                now_sleve[temp] = 0
                temp += i

    return now_sleve

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    sleve = prime_sleve()
    count = 0
    for now_num in num_list:
        if sleve[now_num] == 1:
            count += 1

    print(count)
