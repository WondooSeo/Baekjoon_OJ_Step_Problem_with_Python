import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    crot_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for now_alp in crot_alp:
        word = word.replace(now_alp, '*')

    print(len(word))
