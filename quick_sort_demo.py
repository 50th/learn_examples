"""快速排序算法"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_arr = [i for i in arr if i < pivot]
        equal_arr = [i for i in arr if i == pivot]
        great_arr = [i for i in arr if i > pivot]
        return quick_sort(less_arr) + equal_arr + quick_sort(great_arr)


if __name__ == '__main__':
    example = [3, 6, 8, 10, 1, 2, 1]
    print("原数组:", example)
    print("排序后:", quick_sort(example))
