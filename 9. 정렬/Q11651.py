import sys

if __name__ == '__main__':
    coord = list()
    for N in range(int(sys.stdin.readline().rstrip())):
        coord.append(list(map(int, sys.stdin.readline().rstrip().split())))

    coord.sort(key=lambda x:(x[1], x[0]))
    for now_coord in coord:
        print(*now_coord)
