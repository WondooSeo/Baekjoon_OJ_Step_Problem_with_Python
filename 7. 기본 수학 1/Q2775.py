import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        total_floor_room = [list(range(1, n+1))]
        for i in range(k):
            now_floor_room = [1]
            for j in range(n-1):
                now_floor_room.append(total_floor_room[i][j+1] + now_floor_room[j])
            total_floor_room.append(now_floor_room)

        print(total_floor_room[k][n-1])
