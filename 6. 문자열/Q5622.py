import sys

if __name__ == '__main__':
    dial_input = sys.stdin.readline().rstrip()
    dial_chr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0

    for now_dial in dial_input:
        for i in range(len(dial_chr)):
            if now_dial in dial_chr[i]:
                time += i + 3
                continue

    print(time)
