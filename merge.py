n = int(input())
input_sequence = list(map(int, input().split()))


def merge(sequence, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge(sequence, start, mid)
        merge(sequence, mid, end)
        merge_list(sequence, start, mid, end)
    return ' '.join(map(str, sequence))


def merge_list(sequence, start, mid, end):
    left = sequence[start:mid]
    right = sequence[mid:end]
    k = start
    i, j = 0, 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            sequence[k] = left[i]
            i += 1
        else:
            sequence[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        while k < end:
            sequence[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            sequence[k] = right[j]
            j += 1
            k += 1


print(merge(input_sequence, 0, n))
