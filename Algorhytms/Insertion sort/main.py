def insertion_sort(unsorted_list:list) -> list:
    indexing_length = range(0, len(unsorted_list))
    for i in indexing_length:
        value_to_sort = unsorted_list[i]

        while unsorted_list[i - 1] > value_to_sort and i > 0:
            unsorted_list[i], unsorted_list[ i - 1] = unsorted_list[ i - 1], unsorted_list[i]
            i -= 1

    return unsorted_list


if __name__ == "__main__":
    print(insertion_sort([8, 7, 22, 8, 14, 99, 12]))