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
        print("Tails")

#Fibonacci
def fibonacci(n):
    a, b = 0, 1
    if n <= a:
        result = 0
    elif n == b:
        result = 1
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        result = b
    return result

#Search for an element
def search(array, value):
    if value in array:
        return "Value Exists"
    return "Value doesn't exist"

#Linear search
def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return "Value doesn't exist"

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

#most occuring in a list
def most_occured(array):
    return max(set(array), key = array.count)

#Stack, Queue implementation using list
class StackandQueue:
    def __init__(self):
        self.list = list()
    def add(self, value):
        if value not in self.list:
            self.list.append(value)
            return f"Updated list is : {self.list}"
        return f"Element {value} is already present"
    def lifo(self):
        if len(self.list) > 0:
            self.list.pop()
            return f"Updated List is : {self.list}"
        return f"List is empty"
    def fifo(self):
        if len(self.list) > 0:
            self.list.pop(0)
            return f"Updated list is : {self.list}"
        return f"List is empty"

# Hackerrank List challenge
N = int(input())
arr = list()
arr2 = list()
for i in range(0, N):
    inp = input().split(" ")
    if inp[0] == "insert":
        arr.insert(int(inp[1]), int(inp[2]))
    if inp[0] == "append":
        arr.append(int(inp[1]))
    if inp[0] == "remove":
        arr.remove(int(inp[1]))
    if inp[0] == "sort":
        arr.sort()
    if inp[0] == "pop":
        arr.pop()
    if inp[0] == "reverse":
        arr.reverse()
    if inp[0] == "print":
        arr2 = arr.copy()
        print(arr2)
        arr2.clear()


if __name__ == "__main__":
