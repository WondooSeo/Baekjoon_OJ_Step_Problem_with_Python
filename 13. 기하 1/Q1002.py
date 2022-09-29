import sys

if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
        turret_dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
        elif turret_dist > r1+r2:
            print(0)
        elif turret_dist == r1+r2:
            print(1)
        elif r1+r2 > turret_dist > abs(r1-r2):
            print(2)
        elif turret_dist == abs(r1-r2):
            print(1)
        else:
            print(0)
