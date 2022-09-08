import sys

def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list

    mid = len(input_list)//2
    left_list = merge_sort(input_list[:mid])
    right_list = merge_sort(input_list[mid:])
    merged_list = list()
    left = right = 0

    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            merged_list.append(left_list[left])
            left += 1
        else:
            merged_list.append(right_list[right])
            right += 1

    # Add remainder of left_list and right_list
    merged_list += left_list[left:]
    merged_list += right_list[right:]
    return merged_list

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list()
    for _ in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    sorted_list = merge_sort(num_list)
    print(*sorted_list, sep='\n')
