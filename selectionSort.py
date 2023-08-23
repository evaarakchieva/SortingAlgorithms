def selection_sort(size, input_array):
    array = input_array[:]
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]
    res = ' '.join(map(str, array))
    return res


n = int(input())
lst = list(map(int, input().split()))
print(selection_sort(n, lst))
