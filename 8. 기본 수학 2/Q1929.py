import sys

def prime_sleve(n) -> list:
    now_sleve = [1 for _ in range(n+1)]
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        if now_sleve[i] == 1:
            temp = i*2
            while temp <= n:
                now_sleve[temp] = 0
                temp += i

    return now_sleve

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().rstrip().split())
    sleve = prime_sleve(N)
    for j in range(M, N+1):
        if sleve[j] == 1:
            print(j)
