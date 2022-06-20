import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    room_count, stage = 1, 1

    while room_count < N:
        room_count += stage * 6
        stage += 1

    print(stage)
