import sys


def main():
    card_n = get_number()

    # Calling luhn's function
    luhns_algorithm(card_n)


# Getting user input for card number
def get_number():
    while True:
        try:
            number = input("Enter your card number to check if it is a VALID credit card or INVALID: ")
            if len(number) > 0 and int(number):
                break
        except ValueError:
            continue
    return number


# Implementing Luhn's Algorithm
def luhns_algorithm(number):
    if len(number) < 13 or len(number) > 16:
        print("INVALID")
        sys.exit(0)

    # Even number for even numbers starting from the second last digit
    # Odd numbers for the rest of the remaining numbers in odd places
    even, odd = 0, 0

    # Implementing the algorithm
    if len(number) % 2 == 0:
        for i in range(len(number)):
            num = int(number[i])
            if i % 2 == 0:
                multiply = num * 2
                if multiply >= 10:
                    even += multiply // 10
                    even += multiply % 10
                else:
                    even += multiply
            else:
                odd += num

    else:
        for i in range(len(number)):
            num = int(number[i])
            if i % 2 != 0:
                multiply = num * 2
                if multiply >= 10:
                    even += multiply // 10
                    even += multiply % 10
                else:
                    even += multiply
            else:
                odd += num

    # Getting the last digit of the total sum
    result = (even + odd) % 10

    # Finding the company of the valid card
    if result == 0:
        first = int(number[0])
        second = int(number[1])
        if first == 3 and second == 4 or second == 7:
            print("AMEX")
            sys.exit(0)
        elif first == 5 and 1 <= second <= 5:
            print("MASTERCARD")
            sys.exit(0)
        elif first == 4:
            print("VISA")
            sys.exit(0)
        else:
            print("INVALID")
            sys.exit(0)

    # If not valid
    else:
        print("INVALID")
        sys.exit(0)


main()