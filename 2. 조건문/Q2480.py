import sys

if __name__ == '__main__':
    dice1, dice2, dice3 = map(int, sys.stdin.readline().rstrip().split())

    if dice1 == dice2 == dice3:
        print(dice1*1000 + 10000)
    elif dice1 == dice2:
        print(dice1*100 + 1000)
    elif dice2 == dice3:
        print(dice2*100 + 1000)
    elif dice3 == dice1:
        print(dice3*100 + 1000)
    else:
        print(max(dice1, dice2, dice3)*100)
