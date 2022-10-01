import sys

def dist(a1, b1, a2, b2) -> float:
    return ((a1-a2)**2 + (b1-b2)**2)**0.5

def is_player_in(w, h, x, y, nx, ny) -> bool:
    r = h/2
    if (x <= nx <= x+w and y <= ny <= y+h) or dist(x, y+r, nx, ny) <= r or dist(x+w, y+r, nx, ny) <= r:
        return True
    else:
        return False

if __name__ == '__main__':
    W, H, X, Y, P = map(int, sys.stdin.readline().rstrip().split())
    count = 0
    for _ in range(P):
        now_x, now_y = map(int, sys.stdin.readline().rstrip().split())
        if is_player_in(W, H, X, Y, now_x, now_y):
            count += 1

    print(count)
