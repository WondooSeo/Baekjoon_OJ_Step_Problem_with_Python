import sys

def recur(n):
    if n == 1:
        return ['*']

    recur_star = recur(n//3)
    now_star = list()
    for now_recur_star in recur_star:
        now_star.append(now_recur_star*3)
    for now_recur_star in recur_star:
        now_star.append(now_recur_star + ' '*(n//3) + now_recur_star)
    for now_recur_star in recur_star:
        now_star.append(now_recur_star*3)

    return now_star

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    star = recur(N)
    print(*star, sep='\n')
