def selection_sort(unsorted_list:list) -> list:
    indexing_length = range(0, len(unsorted_list) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(unsorted_list)):
            # If you wish to turn to descending order than swap to greater-than
            if unsorted_list[j] < unsorted_list[min_value]:
                min_value = j

        if min_value != i:
            unsorted_list[min_value], unsorted_list[i] = unsorted_list[i], unsorted_list[min_value]

    return unsorted_list


if __name__ == "__main__":
    print(selection_sort([8, 9, 1, 6, 5, 11, 56, 23]))