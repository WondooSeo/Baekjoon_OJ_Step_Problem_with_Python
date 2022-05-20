import sys

if __name__ == '__main__':
    x = int(sys.stdin.readline().rstrip())
    y = int(sys.stdin.readline().rstrip())

    if x > 0:
        print(1) if y > 0 else print(4)
    else:
        print(2) if y > 0 else print(3)
        