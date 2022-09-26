import sys

def merge_sort(in_A, start, end):
    if start < end:
        mid = (start + end)//2
        merge_sort(in_A, start, mid)
        merge_sort(in_A, mid+1, end)
        merge(in_A, start, mid, end)

def merge(in_A, start, mid, end):
    i, j = start, mid+1
    temp = list()
    while i <= mid and j <= end:
        if in_A[i] <= in_A[j]:
            temp.append(in_A[i])
            i += 1
        else:
            temp.append(in_A[j])
            j += 1

    while i <= mid:
        temp.append(in_A[i])
        i += 1
    while j <= end:
        temp.append(in_A[j])
        j += 1

    i, t = start, 0
    while i <= end:
        A[i] = temp[t]
        i += 1
        change_A.append(temp[t])
        t += 1

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    change_A = list()
    merge_sort(A, 0, N-1)
    print(change_A[K-1] if len(change_A) >= K else -1)
