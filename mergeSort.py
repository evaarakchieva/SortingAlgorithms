def merge_two_sequences(size1, list1, size2, list2):
    i, j = 0, 0
    res = []
    while i < size1 and j < size2:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:]
    res += list2[j:]
    return res


def merge_sort(size, list1, list2):
    sizes = list1
    lists = list2
    if size == 1:
        return ' '.join(map(str, lists[0]))
    for ind in range(size - 1):
        lists[ind + 1] = merge_two_sequences(sizes[ind], lists[ind], sizes[ind + 1], lists[ind + 1])
    sorted_sequence = lists[-1]
    return ' '.join(map(str, sorted_sequence))


n = int(input())
list_of_sizes = []
list_of_sequences = []

for k in range(n):
    list_of_sizes.append(int(input()))
    list_of_sequences.append(list(map(int, input().split())))

print(merge_sort(n, list_of_sizes, list_of_sequences))
