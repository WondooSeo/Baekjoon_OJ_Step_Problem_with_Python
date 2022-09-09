import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    count, dest = 1, 666
    while count < N:
        dest += 1
        if '666' in str(dest):
            count += 1

    print(dest)
