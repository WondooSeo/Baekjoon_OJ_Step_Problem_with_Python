import sys

def prime_sleve(n) -> list:
    now_sleve = [1 for _ in range(n+1)]
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        if now_sleve[i] == 1:
            temp = i * 2
            while temp <= n:
                now_sleve[temp] = 0
                temp += i

    prime_list = list()
    for i in range(n+1):
        if now_sleve[i] == 1:
            prime_list.append(i)

    return prime_list


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    prime = prime_sleve(N)
    for now_prime in prime:
        while N%now_prime == 0:
            print(now_prime)
            N = N//now_prime
