import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
    dict_X = dict()
    sorted_X = sorted(list(set(X)))
    for i in range(len(sorted_X)):
        dict_X[sorted_X[i]] = i

    for now_X in X:
        print(dict_X[now_X], end=' ')
