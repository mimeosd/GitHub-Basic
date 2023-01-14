def prime_number(number:int) -> bool:
    """
    Returns True if the number is prime, and False if it is not
    
    :param number: the number to be checked
    :type number: int
    :return: True or False
    """
    for i in range(2, ((number//2)+1)):
        if number % i == 0:
            return False
    return True


def dividers_of_a_number(neki_broj:int) -> list:
    """
    Returns a list of all the numbers that divide the input number
    
    :param neki_broj: int - the number you want to find the dividers of
    :type neki_broj: int
    :return: A list of all the divisors of the number.
    """
    res_list = []
    for i in range(2, neki_broj//2):
        if neki_broj % i == 0:
            res_list.append(i)
    return res_list


if __name__ == "__main__":
    maximum = 0
    for i in dividers_of_a_number(13195):
        if prime_number(i) == True:
            maximum = i
        elif prime_number(i) == False:
            pass
    print(maximum)
