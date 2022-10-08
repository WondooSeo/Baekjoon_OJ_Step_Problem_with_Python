import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    rad_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N-1):
        now_gcd = gcd(rad_list[0], rad_list[i+1])
        print(f'{rad_list[0]//now_gcd}/{rad_list[i+1]//now_gcd}')
