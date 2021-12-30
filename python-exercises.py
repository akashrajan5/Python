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

#class Examples
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def fullname(self):
        return '{} and model is {}'.format(self.name, self.model)

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

#Scraping
def scraping(url):
    #url = 'https://flea.today/store/'
    import requests
    from bs4 import BeautifulSoup
    txt = open("scraping.txt", "w")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    main = soup.find(class_="main-product")
    img = main.find_all('img', class_="fami-img")
    for i in img:
        print(i['data-src'])


if __name__ == "__main__":
    print(headsTails(5))