import sys

def prime_sleve() -> list:
    N = 10000
    now_sleve = [1 for _ in range(N+1)]
    return_sleve = list()
    now_sleve[0], now_sleve[1] = 0, 0
    for i in range(2, int(N**0.5)+1):
        if now_sleve[i] == 1:
            temp = i*2
            while temp <= N:
                now_sleve[temp] = 0
                temp += i

    for i in range(N+1):
        if now_sleve[i] == 1:
            return_sleve.append(i)

    return return_sleve

if __name__ == '__main__':
    sleve = prime_sleve()
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        l_num, r_num = n//2, n//2
        while l_num > 0:
            if l_num in sleve and r_num in sleve:
                print(l_num, r_num)
                break

            l_num -= 1
            r_num += 1
