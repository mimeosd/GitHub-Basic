def bubble_sort(any_list:list) -> list: 
    
    # Putting an anchor here since you can not compare last element or you would get Indexing error
    indexing_length = len(any_list) - 1
    main_flag = False

    while not main_flag:
        main_flag = True
        for i in range(0, indexing_length):
            if any_list[i] > any_list[i + 1]:
                main_flag = False
                any_list[i], any_list[i + 1] = any_list[i + 1], any_list[i]
    return any_list


if __name__ == "__main__":
    print(bubble_sort([1, 55, 12, 7, 9, 44, 12]))