#!/usr/bin/env python3.7

def cls(): print ("\n" * 50)
cls()

import sys
print(sys.version)

integerNumber = 10
floatingNumber = 10.50
print(type(integerNumber))
print(type(floatingNumber))
print(floatingNumber)
floatingNumber = int(floatingNumber)
print(type(floatingNumber))
print(floatingNumber)

string = "bonjour victor"
print(string.upper())
print(string.lower())
print(string.title()) # first letter is upper-case
print(string.replace("bonjour", "salut").title())
print(string[0:3]) # slicing
print(len(string))
print(string.find('victor'))

print("   Some extra spaces were here   ".strip())
print("   Some extra spaces were here at the left".lstrip())
print("Some extra spaces were here at the right       ".rstrip())

print("101 Main Street \tMontreal")
print("101 Main Street \nMontreal")

# returns float, 5.0
print(10 / 2)
# returns int, 5
print(10 // 2)
# modulo, 5
print(15 % 10)
# exponent
print(2**3)

# list
favoriteFruits = ['Apple', 'Mango', 'Orange']
print(favoriteFruits)
print(favoriteFruits[2])
favoriteFruits[2] = 'Melon'
print(favoriteFruits)
favoriteFruits.append('Kiwi')
print(favoriteFruits)
favoriteFruits.insert(1, 'Strawberry')
print(favoriteFruits)
favoriteFruits.remove('Strawberry')
print(favoriteFruits)
favoriteFruits.sort()
print(favoriteFruits)
favoriteFruits.reverse()
print(favoriteFruits)
favoriteFruits.pop() # return last element and remove it
print(favoriteFruits)

# tuple
historicWarDates = ('1914', '1939')
print(historicWarDates[0])
del(historicWarDates)
print(historicWarDates)

# dictionary
priceOfCameras = {"Sony": 500, "Nikon": 600, "Canon": 700}
print(priceOfCameras)
print(priceOfCameras["Sony"])
priceOfCameras["Nikon"] = 1000
print(priceOfCameras["Nikon"])
print(priceOfCameras.keys())
print(priceOfCameras.values())
copyOfPriceOfCameras = priceOfCameras.copy()
del priceOfCameras["Sony"]
print(priceOfCameras)
priceOfCameras.clear()

number = int(input("Enter a number:"))
if number % 3 is 0:
    print("Number is a multiple of 3")
    if number % 7 is 0:
        print("Number is also a multiple of 7")
    else:
        print("Number is a multiple of 3, but not a multiple of 7")

fruits = ['Apple', 'Mango', 'Orange', 'Strawberry']
for fruit in fruits:
    print(fruit)

for number in range(1, 11):
    print(number)

temperature = 77
while temperature >= 68 and temperature <= 77:
    print("Room temperature is {}".format(temperature))
    temperature = temperature - 1

# matrix
number = 1
for row in range(1, 4):
    for columne in range(1, 4):
        print(number, end = ' ')
        number = number + 1
    print()

for number in range(1, 11):
    if number == 5:
        continue
    else:
        print(number)

for number in range(1, 11):
    if number == 15:
        break
    else:
        print(number)
else:
    print("All the numbers were printed without breaking the loop!")

collectionOfBooks = ["War and Peace", "Les Rois maudits", "Anna Karenina", "Trois mousquetaires", "Inferno"]
print("Enter the name of the book: ")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes, I do have this book")
        break
else:
    print("I do not have this book")

def helloWorld():
    print("Hello, World")
helloWorld()

# area = length * widht
lenghtOne = 8
widthOne = 3
areaOne = lenghtOne * widthOne
print(areaOne)
lenghtTwo = 10
widthTwo = 4
areaTwo = lenghtTwo * widthTwo
print(areaTwo)
def computeArea(lenght, width):
    area = lenght * width
    return area
computeArea(lenghtOne, widthOne)
computeArea(lenghtTwo, widthTwo)
askLength = float(input("Enter lenght:"))
askWidth = float(input("Enter width:"))
print(computeArea(askLength, askWidth))

# maximum number
def findMaximum(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        print("First number is greater")
        return firstNumber
    elif secondNumber > firstNumber:
        print("Second number is greater")
        return secondNumber
    else:
        print("Both the numbers are equal")
        return firstNumber
print("Enter the first number:")
firstNumber = int(input())
print("Enter the second number:")
secondNumber = int(input())
maximumNumber = findMaximum(firstNumber, secondNumber)
print("Maximum number = {}".format(maximumNumber))

try:
    length = 10
    width = 0
    length / width
except ZeroDivisionError:
    print("Division by 0 is invalid! Kindly change your input.")
try:
    length / notDefined
except NameError:
    print("Variable has been used before defining it.")
