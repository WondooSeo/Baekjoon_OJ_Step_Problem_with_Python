import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        now_case = sys.stdin.readline().rstrip()
        now_score, now_streak = 0, 0

        for now_ans in now_case:
            if now_ans == 'O':
                now_streak += 1
                now_score += now_streak
            else:
                now_streak = 0

        print(now_score)
