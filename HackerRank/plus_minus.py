
class Solution(object):

    def plus_minus(self, n, arr):

        # something to track the values we want to record
        # positive, negative, zero
        count_dict = {
            -1: 0,
            0: 0,
            1: 0
        }

        # logic to loop through and count
        for val in arr:
            if val < 0:
                count_dict[-1] += 1
            elif val == 0:
                count_dict[0] += 1
            else:
                count_dict[1] += 1

        # logic to display outputs
        for i in [1, -1, 0]:
            str = '{:.6f}'.format(round(count_dict[i] / n, 6))
            print(str)
            
        # Want to return 'not a number'    
        return None

if __name__ == "__main__":
    a = Solution()
    arr = [-4, 3, -9, 0, 4, 1]
    n = 6

    a.plus_minus(n, arr)
