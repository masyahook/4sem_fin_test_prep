def merge_sort(A):
    def merge(L, R):
        A = [None] * (len(L) + len(R))
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        A[k:] = L[i:] + R[j:]
        return A
    len_a = len(A)
    if len_a <= 1:
        return A
    mid = len_a // 2
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))


n = int(input())
using_list = list(map(int, input().split()))
evens, odds = [], []
for elem in using_list:
    if elem % 2 == 0:
        evens.append(elem)
    else:
        odds.append(elem)
print(' '.join(map(str, merge_sort(odds) + merge_sort(evens)[-1::-1])))
