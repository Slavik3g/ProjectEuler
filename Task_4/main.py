def isPalindrome(num: int) -> bool:
    str_num = str(num)
    return str_num == str_num[::-1]


def maxPalindrome(power: int) -> int:
    max_palindrome = 0
    for i in range(10**power, 10**(power-1), -1):
        for j in range(10 ** power, i, -1):
            multiplication = j * i
            if multiplication <= max_palindrome:
                break
            if isPalindrome(multiplication) and multiplication > max_palindrome:
                max_palindrome = multiplication
    return int(max_palindrome)


def run():
    print(maxPalindrome(3))


if __name__ == '__main__':
    run()
