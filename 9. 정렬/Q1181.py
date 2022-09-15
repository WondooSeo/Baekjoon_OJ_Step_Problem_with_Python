import sys

if __name__ == '__main__':
    word_list = list()
    for N in range(int(sys.stdin.readline().rstrip())):
        word_list.append(sys.stdin.readline().rstrip())

    word_list = list(set(word_list))
    word_list.sort(key=lambda x: (len(x), x))
    print(*word_list, sep='\n')
