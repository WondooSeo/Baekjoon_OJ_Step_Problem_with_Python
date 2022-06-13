import sys

if __name__ == '__main__':
    # Using dictionary
    # now_str = sys.stdin.readline().rstrip().upper()
    # alpha_dict = dict()
    #
    # for now_chr in now_str:
    #     if now_chr not in alpha_dict:
    #         alpha_dict[now_chr] = 1
    #     else:
    #         alpha_dict[now_chr] += 1
    #
    # total_num_alp = sorted(alpha_dict.items(), key=lambda x: -x[1])
    #
    # if len(total_num_alp) > 1 and total_num_alp[0][1] == total_num_alp[1][1]:
    #     print('?')
    # else:
    #     print(total_num_alp[0][0])

    # Using set and count
    now_str = sys.stdin.readline().rstrip().upper()
    unique_chr = list(set(now_str))
    count_list = list()

    for now_chr in unique_chr:
        count_list.append(now_str.count(now_chr))

    if count_list.count(max(count_list)) > 1:
        print('?')
    else:
        print(unique_chr[count_list.index(max(count_list))])
