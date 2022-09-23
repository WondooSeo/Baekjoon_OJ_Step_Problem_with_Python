import sys

if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    len_S, subset_S = len(S), set()
    for i in range(1, len_S+1):
        for j in range(len_S-i+1):
            subset_S.add(S[j:j+i])

    print(len(subset_S))
