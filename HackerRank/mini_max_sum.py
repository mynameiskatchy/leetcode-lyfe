"""

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.

"""


def miniMaxSum(arr):
    # Write your code here

    total = sum(arr)
    max = 0
    min = total
    # is arr sorted? 

    # logic to update values by subtracting single value from total
    # update depending on
    # if we find higher sum for max
    # if we find lower sum for min
    for val in arr:
        if total - val < min:
            min = total - val
        if total - val > max:
            max = total - val

    print('{} {}'.format(min, max))

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)

    """
    total = 1 + 2 + 3 + 4 + 5 = 15, max = 0, min = 15

    val = 1
    min = 14
    max = 14

    val = 2
    min = 13
    max = 14

    val = 3
    min = 12
    max = 14

    .
    .
    .

    val = 5
    min = 10
    max = 14

    """


    