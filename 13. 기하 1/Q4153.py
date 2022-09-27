import sys

if __name__ == '__main__':
    while True:
        tc = list(map(int, sys.stdin.readline().rstrip().split()))
        if tc == [0, 0, 0]:
            break

        tc.sort()
        if tc[2]**2 == tc[0]**2 + tc[1]**2:
            print('right')
        else:
            print('wrong')
