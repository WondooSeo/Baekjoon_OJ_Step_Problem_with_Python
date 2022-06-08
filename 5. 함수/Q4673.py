def d(n):
    m = n + sum(map(int, str(n)))
    return m


if __name__ == '__main__':
    self_num_set = set(range(10001))
    non_self_num_set = set()
    for i in range(1, 10001):
        non_self_num_set.add(d(i))

    self_num_list = sorted(list(self_num_set - non_self_num_set))
    for now_self_num in self_num_list[1:]:
        print(now_self_num)
