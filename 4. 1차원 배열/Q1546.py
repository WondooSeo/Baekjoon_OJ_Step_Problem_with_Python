import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    score_list = list(map(int, sys.stdin.readline().rstrip().split()))

    print(sum(score_list)/max(score_list)*100/N)
