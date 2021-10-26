def diagonalDifference(arr):
    # Write your code here
    sum_left = 0
    sum_right = 0

    for i in range(len(arr)):
        # logic to add left diagonal
        sum_left += arr[i][i]
        #logic for right diagonal
        sum_right += arr[i][-i-1]

    # calculate abs(left - right sums)
    ab = abs(sum_left - sum_right)
    return ab

if __name__ == "__main__":
    
    arr = [
     [1, 2, 3],
     [4, 5, 6],
     [9, 8, 9],
    ]

    out = diagonalDifference(arr)
    print(out)
    pass
