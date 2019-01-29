### KEY: 0 POINTS
### KEY: Close, but no solutions produce the expected results 

# Python Review Misc Topics

### Problem 1:
Given a number n, return ```True``` if n is in the range 1..10, inclusive. Unless outside_mode is ```True```, in which case return True if the number is less or equal to 1, or greater or equal to 10. Print the result returned from your function.

BONUS: Get the number and outside_mode flag from User input instead of hardcoding it

```def in1to10(n, outside_mode):```

Examples of Expected Output:

```in1to10(5, False)``` → True

```in1to10(11, False)``` → False

```in1to10(11, True)``` → True


### Problem 2:
##### We will keep having (some variation) of this problem until EVERYONE gets it right without help
Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.

Once the user enters the equal sign to quit, print all the strings that were entered as one line with each word separated by a comma and space.

Example of Expected Output:

```You, Entered, These, Words, Today```

### Problem 3:
Given a non-negative number "num", return ```True``` if num is within ```2``` of a *multiple of 10*. Print the result from your function.

BONUS: Get the number from User input instead of hardcoding it

```def near_ten(num):```

Examples of Expected Output:

```near_ten(12)``` → True

```near_ten(17)``` → False

```near_ten(19)``` → True

### Problem 4:
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: There isn't any restriction on how your approach determining what the min and max values are.

```def big_diff(nums):```

Examples of Expected Output:

```big_diff([10, 3, 5, 6])``` → 7

```big_diff([7, 2, 10, 9])``` → 8

```big_diff([2, 10, 7, 2])``` → 8
