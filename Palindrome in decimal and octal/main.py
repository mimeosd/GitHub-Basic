
def decimal_to_octal(number:int) -> str:
    octal = ''
    while number > 0:
        octal = str(number % 8) + octal
        number //= 8
    return octal


def provera_oktalnog_palindroma(some_string:str) -> bool:
    if some_string == some_string[::-1]:
        return True


def checking_of_decimal_palindrome(neki_broj:int) -> bool:
    if str(neki_broj) == str(neki_broj)[::-1]:
        return True


def main_f(_range:int) -> dict:
    res_dict = {}
    for i in range(1, _range):
        if checking_of_decimal_palindrome(i) == True and provera_oktalnog_palindroma(decimal_to_octal(i)) == True:
            res_dict[i] = decimal_to_octal(i)
    return res_dict

if __name__ == "__main__":
    print(main_f(1000000))