def quicksort(unsorted_list:list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    else:
        pivot_point = unsorted_list.pop()

    less_than = []
    greater_than = []

    for i in unsorted_list:
        if i <= pivot_point:
            less_than.append(i)
        
        else:
            greater_than.append(i)

    return quicksort(less_than) + [pivot_point] + quicksort(greater_than)



if __name__ == "__main__":
    print(quicksort([1, 66, 5, 312, 65, 9, 97, 60]))