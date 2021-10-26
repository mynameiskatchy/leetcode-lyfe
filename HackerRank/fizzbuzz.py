# fizzbuzz: i -> None
# effects: i -> Str

def fizzbuzz(n):

    # if multiple of 3 & 5 -> FizzBuzz
    # if multiple of 3 (not 5) -> Fizz
    # if multiple of 5 (not 3) -> Buzz

    outputs = {
        3: 'Fizz',
        5: 'Buzz'
    }

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(outputs[3] + outputs[5])
        elif i % 3 == 0:
            print(outputs[3])
        elif i % 5 == 0:
            print(outputs[5])
        else:
            print(i)

    return None

fizzbuzz(15)