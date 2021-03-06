# Finding the highest of three numbers
from distutils.errors import LinkError
from unittest.mock import NonCallableMagicMock


def highest_of_three(a, b, c):
    if a > b and a > c:
        result = f'{a} is greater'
    elif b > a and b > c:
        result = f'{b} is greater'
    else:
        result = f'{c} is greater'
    return result

# Function to reverse a string
def strRevUsingSlice(e):
    print(e[::-1])

# Reverse a string
def revUsingLoop(e):
    s = ""
    for i in e:
        s = i + s
    print(s)

# FizzBuzz program
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

# Fibonacci
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

# Search for an element
def search(array, value):
    if value in array:
        return "Value Exists"
    return "Value doesn't exist"

# Linear search
def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return "Value doesn't exist"

# Binary search -> Iterative
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

# Most occuring in a list
def most_occured(array):
    return max(set(array), key = array.count)

# Stack, Queue implementation using list
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
        return "List is empty"
    def fifo(self):
        if len(self.list) > 0:
            self.list.pop(0)
            return f"Updated list is : {self.list}"
        return "List is empty"

# Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        low = i
        for j in range(i+1, len(arr)):
            low = j if arr[j] < arr[low] else low
        arr[i], arr[low] = arr[low], arr[i]
    return arr

# Bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# diagonal difference
def diagonalDifference(arr):
    first = second = 0
    for i in range(len(arr)):
        first += arr[i][i]
        second += arr[i][len(arr) - i - 1]
    return abs(first - second)

# Linked list 
class LinkedListNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # insert at beginning
    def AtBeginning(self, data = None):
        if data is not None:
            newNode = LinkedListNode(data)
            newNode.next = self.head
            self.head = newNode
        else:
            return "Value is none"
    # insert at end
    def AtEnd(self, newdata):
        newNode = LinkedListNode(newdata)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    # insert inbetween
    def InBetween(self, middlenode, newdata):
        if middlenode is None:
            return "Sepcify a middle node"
        newnode = LinkedListNode(newdata)
        newnode.next = middlenode.next
        middlenode.next = newnode
    # delete a node
    def DeleteNode(self, value):
        temp = self.head
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
    # print linked list
    def PrintList(self):
        dataval = self.head
        while dataval:
            print(dataval.data)
            dataval = dataval.next
        
# tree data structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # insert into a tree
    def insert(self, data):
        if self.data:
            # need to be accurate
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
            pass #TODO
        else:
            self.data = data
    # print tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()



if __name__ == "__main__":
    # Llist = LinkedList()
    # Llist.head = LinkedListNode(3)
    # second = LinkedListNode(5)
    # third = LinkedListNode(1)
    # Llist.head.next = second
    # second.next = third
    # Llist.AtBeginning(10)
    # Llist.AtEnd(9)
    # Llist.InBetween(Llist.head,8)
    # Llist.DeleteNode(8)
    # Llist.PrintList()
    pass