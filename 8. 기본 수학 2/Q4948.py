import sys

def prime_sleve() -> list:
    N = 123456*2
    now_sleve = [1 for _ in range(N+1)]
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(N**0.5)+1):
        if now_sleve[i] == 1:
            temp = i*2
            while temp <= N:
                now_sleve[temp] = 0
                temp += i

    return now_sleve

if __name__ == '__main__':
    sleve = prime_sleve()
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            break

        print(sleve[n+1:2*n+1].count(1))
