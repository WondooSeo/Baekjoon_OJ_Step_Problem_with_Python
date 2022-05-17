import sys

if __name__ == '__main__':
    now_score = int(sys.stdin.readline().rstrip())

    if 90 <= now_score <= 100:
        print('A')
    elif 80 <= now_score <= 89:
        print('B')
    elif 70 <= now_score <= 79:
        print('C')
    elif 60 <= now_score <= 69:
        print('D')
    else:
        print('F')
