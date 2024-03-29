import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list()
    for _ in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))
    num_list.sort()
    now_gcd = num_list[1] - num_list[0]
    for i in range(1, N-1):
        now_gcd = gcd(now_gcd, abs(num_list[i+1]-num_list[i]))

    yaksu = {now_gcd}
    for i in range(2, int(now_gcd**0.5)+1):
        if now_gcd%i == 0:
            yaksu.add(i)
            yaksu.add(now_gcd//i)

    print(*sorted(list(yaksu)))
