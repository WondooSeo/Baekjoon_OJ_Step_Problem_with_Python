import sys

if __name__ == '__main__':
    C = int(sys.stdin.readline().rstrip())
    for _ in range(C):
        N_score = list(map(int, sys.stdin.readline().rstrip().split()))
        now_average = sum(N_score[1:]) / N_score[0]
        over_average_num = 0

        for i in range(N_score[0]):
            if N_score[i+1] > now_average:
                over_average_num += 1

        over_average = int(100000*(over_average_num/N_score[0]) + 0.5) / 1000
        print(f'{over_average:.3f}%')
