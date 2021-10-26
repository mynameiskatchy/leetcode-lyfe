def findMedian(arr):


    # length of array to find middle
        # if even then 1/2 of two middle numbers
        # if off then n/2th position
    # sort it
        


    # alternate soln?

    pass

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    pass
