def binary_search(unsorted_list:list, item:int) -> list:
    begin_index = 0
    end_index = len(unsorted_list) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = unsorted_list[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1
    
    return None


if __name__ == "__main__":
    some_list = [1, 3, 5, 7, 9, 11]
    item_to_search = 5
    print(binary_search(some_list, item_to_search))

