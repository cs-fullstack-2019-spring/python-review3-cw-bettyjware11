def main():  # point of entry
    Problem1()
    # Problem2()
    # Problem3()
    # Problem4


# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number
# is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function.
# BONUS: Get the number and outside_mode flag from User input instead of hardcoding it

def Problem1():
    n = int(input("Enter number"))
    outside_mode = int(input("Enter outside mode flag"))
    for n in range(1, 11):
        if (n >= 1 and n <= 10):
            print("True")
        elif outside_mode == "True":
            if (n <= 1 or n >= 10):
                print("True")
    else:
        print("False")


# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
# Once the user enters the equal sign to quit, print all the strings that
# were entered as one line with each word separated by a comma and space.
def Problem2():
    stringList = []
    strings = input("Enter a string")
    while (strings != '='):
        print("Enter another")  # error
        # KEY: Sadly, this overwrites the string every time so keep a separate stringList
        strings = input("Enter string")  # ask again
        if (strings != '='):
            stringList.append(strings)
        else:
            break

    print(','.join(stringList))


# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Print the result from your function.
# BONUS: Get the number from User input instead of hardcoding it
def Problem3():
    num = int(input("Enter number"))
    x = num % 10
    if (10 - (10 - x)) <= 2 or (10 - x) <= 2:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
