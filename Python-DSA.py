#class Examples
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def fullname(self):
        return '{} and model is {}'.format(self.name, self.model)

#Finding the highest of three numbers
def highest_of_three(a, b, c):
    if a > b and a > c:
        result = f'{a} is greater'
    elif b > a and b > c:
        result = f'{b} is greater'
    else:
        result = f'{c} is greater'
    return result

#function to reverse a string
def strRevUsingSlice(e):
    print(e[::-1])

def revUsingLoop(e):
    s = ""
    for i in e:
        s = i + s
    print(s)

#FizzBuzz program
def fizz_buzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        print(i)

# Heads or Tails
def heads_tails(n):
    import random
    for i in range(n):
        if(random.randint(0, 1)):
            print("Heads")
        else:
            print("Tails")

#Fibonacci
def fibonacci(n):
    a, b = 0, 1
    if n <= a:
        return 0
    elif n == b:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b

#Linear search
def linear_search(array, value):
    for i in array:
        if value == i:
            return "Found"
    return "No Value Found"

#Binary search -> Iterative
def binary_search(array, value):
    low, mid, high = 0, 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return "No Value Found"


if __name__ == "__main__":
    print(binary_search([1,3,4,6,8,9,10,18], 9))
