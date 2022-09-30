import sys

def dist(a1, b1, a2, b2):
    return ((a1-a2)**2 + (b1-b2)**2)**0.5

if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        count = 0
        for n in range(int(sys.stdin.readline().rstrip())):
            cx, cy, r = map(int, sys.stdin.readline().rstrip().split())
            dist1, dist2 = dist(x1, y1, cx, cy), dist(x2, y2, cx, cy)
            if dist1 < r:
                count += 1
            if dist2 < r:
                count += 1
            if dist1 < r and dist2 < r:
                count -= 2

        print(count)
