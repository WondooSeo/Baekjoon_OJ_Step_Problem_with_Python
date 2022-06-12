import sys

if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    alp_dict = dict()
    for i in range(26):
        alp_dict[chr(ord('a')+i)] = -1

    for j in range(len(S)):
        if alp_dict[S[j]] == -1:
            alp_dict[S[j]] = j

    print(*alp_dict.values())
