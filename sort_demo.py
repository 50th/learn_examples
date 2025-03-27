def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_arr = [i for i in arr[1:] if i < pivot]
        great_arr = [i for i in arr[1:] if i > pivot]
        return quick_sort(less_arr) + [pivot] + quick_sort(great_arr)
