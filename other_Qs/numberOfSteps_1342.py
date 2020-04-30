""" numberOfSteps
==========================================================================
1342. Number of Steps to Reduce a Number to Zero 
numberOfSteps()
<https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero>
==========================================================================

Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
 

Constraints:

0 <= num <= 10^6

"""

class Solution(object):
    
    def numberOfSteps_recursion (self, num):
        """
        :type num: int
        :rtype: int

        Runtime: 16 ms, faster than 75.53% of Python online submissions for Number of Steps to Reduce a Number to Zero.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Number of Steps to Reduce a Number to Zero
        """

        # Using recursion
        n_steps = 0

        if num == 0:
            return n_steps
        elif ((num % 2) == 0):
            return 1 + self.numberOfSteps_recursion(num/2)
        else:
            return 1 + self.numberOfSteps_recursion(num-1)

        # Using loop
        def numberOfSteps_loop(self, num):
            """
            :type num: int
            :rtype: int
            """

            counter = 0

            while (num > 0):
                if (num % 2) == 0:
                    num /= 2
                else:
                    num -= 1
                counter += 1

            return counter



if __name__ == "__main__":

    in1, out1 = 14, 6
    in2, out2 = 8, 4
    in3, out3 = 123, 12

    def numberOfSteps(num):
        """
        :type num: int
        :rtype: int
        """

        n_steps = 0

        # Using Recursion
        if num == 0:
            return n_steps
        elif num%2 == 0:
            n_steps = 1 + numberOfSteps(num/2)
            return n_steps
        else:
            n_steps = 1 + (numberOfSteps(num-1))
            return n_steps




    # Tests
    print(numberOfSteps(in1))
    print(numberOfSteps(in2))
    print(numberOfSteps(in3))
    
    print('Hello Word')

    
