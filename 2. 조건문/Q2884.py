import sys

if __name__ == '__main__':
    H, M = map(int, sys.stdin.readline().rstrip().split())

    if M < 45:
        alarm_M = M + 15
        alarm_H = H - 1
        if alarm_H < 0:
            alarm_H = 23

    else:
        alarm_M = M - 45
        alarm_H = H

    print(alarm_H, alarm_M)
