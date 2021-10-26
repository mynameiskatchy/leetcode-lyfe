def lonelyinteger(a):
    # Write your code here

    # dictionary to track # occurances
    instances = dict()

    # loop through array to count
    for n in a:
        # if the value is in dictionary, +=1 occurances
        if n in instances:
            instances[n] += 1
        # if not, add value: 1
        else:
            instances[n] = 1

    for key, val in instances:
        print(key, val)
        if val == 1:
            return key


def lonelyinteger(a):
    # Write your code here

    # dictionary to track # occurances
    instances = dict()

    # loop through array to count
    sum = 0
    for n in a:
        # if the value is in dictionary, +=1 occurances
        # if n in instances:
        #     instances[n] += 1
        # # if not, add value: 1
        # else:
        #     instances[n] = 1
        sum ^= n
    return sum

    # for key, val in instances.items():
    #     if val == 1:
    #         return key


if __name__ == "__main__":
    arr1 = [1, 2, 3, 2, 3]
    arr2 = [5, 4, 3, 4, 5]

