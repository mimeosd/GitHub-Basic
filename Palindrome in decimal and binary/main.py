

def generator_palindromes_decimal(broj:int) -> bool:
    """Using built-in functions"""
    if str(broj) == str(broj)[::-1]:
        return True


def generator_binary_palindromes(neki_str:str) -> bool:
    """Using built-in functions"""
    if neki_str == neki_str[::-1]:
        return True


def generator_palindroma_harder(broj_za_konvertovanje:int) -> str:
    """Manually converting from decimal to binary"""
    result = []
    while (broj_za_konvertovanje != 0):
        temp = broj_za_konvertovanje % 2
        result.append(temp)
        broj_za_konvertovanje = broj_za_konvertovanje // 2
    result.reverse()
    
    res = ""
    for i in result:
        res += str(i)
    return res



def palindrome_checker(domet:int) -> None:
    """Main function for checking results wheter both statements are True.
    Or you can use manual checker (harder variant)
    """
    for i in range(domet):
        if generator_palindromes_decimal(i) == True and generator_binary_palindromes(generator_palindroma_harder(i)) == True:
            print(i)

if __name__ == "__main__":
    palindrome_checker(1000000)