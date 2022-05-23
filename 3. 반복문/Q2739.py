import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    for i in range(1, 10):
        print(f'{N} * {i} = {N*i}')
