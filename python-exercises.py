# Finding the highest of three numbers using command line input.
import sys

try:
    a = len(sys.argv)
    b = int(sys.argv[1])
    c = int(sys.argv[2])
    d = int(sys.argv[3])
    if(a < 4 or a > 4):
        print('Please provide three numbers')
    else:
        if(b > c and b > d):
            print(f'{b} is the highest')
        elif(c > d and c > b):
            print(f'{c} is the highest')
        else:
            print(f'{d} is the highest')
except ValueError:
    print('Please provide integers')

#function to reverse a string

def strRevUsingSlice(e):
    print(e[::-1])

def revUsingLoop(e):
    s = ""
    for i in e:
        s = i + s
    print(s)

#FizzBuzz program
def fizz():
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

#Scraping
import requests
from bs4 import BeautifulSoup

#txt = open("scraping.txt", "w")
url = 'https://flea.today/store/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
main = soup.find(class_="main-product")
img = main.find_all('img', class_="fami-img")
for i in img:
    print(i['data-src'])