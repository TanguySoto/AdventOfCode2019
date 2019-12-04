"""
https://adventofcode.com/2019

Day 4 - Second puzzle

@author Tanguy Soto
@date 04/12/2019 - Darmstadt
"""


def find_possible_passwords_count():
    """
    Brute force count of the number of possible passwords.

    :return int: the count
    """

    start = 444444
    end = 864247

    valid_pwd_count = 0

    for pwd in range(start, end + 1):
        pwd_str = str(pwd)

        previous_digit = int(pwd_str[0])
        sequences_length = [1]
        max_digit = int(pwd_str[0])
        is_increasing = True

        for char in pwd_str[1:]:
            digit = int(char)

            if digit < max_digit:
                is_increasing = False
                break
            max_digit = max(digit, max_digit)

            if digit == previous_digit:
                sequences_length[-1] += 1
            else:
                sequences_length.append(1)

            previous_digit = digit

        if is_increasing and 2 in sequences_length:
            valid_pwd_count += 1

    return valid_pwd_count


if __name__ == '__main__':
    answer = find_possible_passwords_count()

    print("Day4 - second puzzle answer:\n{}".format(answer))
