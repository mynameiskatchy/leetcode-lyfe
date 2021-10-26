def countingSort(arr):
    # Write your code here

    # initialize counting array with zeros
    counter = [0 for i in range(0, 100)]

    for i, val in enumerate(arr):
        counter[val] += 1
    return(counter)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
