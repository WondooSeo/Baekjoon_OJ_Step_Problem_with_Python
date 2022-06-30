import sys

def prime_sleve(N) -> list:
    now_sleve = [1 for _ in range(N+1)]
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(N**0.5)+1):
        if now_sleve[i] == 1:
            temp = i * 2
            while temp <= N:
                now_sleve[temp] = 0
                temp += i

    return now_sleve

if __name__ == '__main__':
    M = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    sleve = prime_sleve(N)
    total_sum, min_prime = 0, -1
    for now_num in range(N, M-1, -1):
        if sleve[now_num] == 1:
            total_sum += now_num
            min_prime = now_num

    if min_prime != -1:
        print(total_sum, min_prime, sep='\n')
    else:
        print(min_prime)
