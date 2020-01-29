import sys
import re


def sum_digits(digit):

#Calculating summation of the double of even index numbers

    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)
    # add the digits if any number is more than 9 (double digit number)
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

if _name_ == "_main_":

    PATTERN = r"^(?!.*([0-9])(?:-?\1){3})[456][0-9]{3}(-?)[0-9]{4}\2[0-9]{4}\2[0-9]{4}$"

    if re.match(PATTERN,sys.argv[1]):
        num=sys.argv[1]
        num=str(num).replace('-','')
        validate(num)
        print('Valid credit Card Number ')

    else:
        print('Not A Valid Credit Card Number')
