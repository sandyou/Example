def quick_sort2(list, left, right): #in-place
    if left >= right:
        return list
    key = list[left]
    left_pivot = left
    right_pivot = right
    while left_pivot < right_pivot:
        while left_pivot < right_pivot and list[right_pivot] >= key: #從左向右找小於key值的
            right_pivot = right_pivot - 1
        while left_pivot < right_pivot and list[left_pivot] <= key: #從右向左找大於key值的
            left_pivot = left_pivot + 1
        if left_pivot < right_pivot:
            list[left_pivot], list[right_pivot] = list[right_pivot], list[left_pivot]
    list[left], list[left_pivot] = list[left_pivot], list[left] #跟key值交換
    quick_sort2(list, left, left_pivot - 1)
    quick_sort2(list, right_pivot + 1, right)
    return list

def quick_sort(list):
    return quick_sort2(list, 0, len(list)-1)

mylist = [20, 9, 100, 0, 55, 3, 11]
print ("result：", quick_sort(mylist))
