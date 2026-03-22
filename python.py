# Create variable
# name = "test"

# print(name)

# create a function which takes an argument

# def squared(number):
#     return number * number

# print(squared(16))

# create a function which adds two numbers together

# def addTogether(firstNumber, secondNumber):
#     return firstNumber + secondNumber

# print(addTogether(12,5))

# create expression for division

# def calculation(num):
#     calculated = (num / 2) +1 
#     return calculated

# print(calculation(5))

# create function to take an argument and carry out multiplication with it

# def calculationTwo(num):
#     calculated = (num * 40) + 60
#     return calculated

# print(calculationTwo(5))

# create function which carries out some calculation

# def calculated(numA, numB):
#     return (numA + numB) * 2

# print(calculated(10, 27))

# def firstLetter(input):
#     return input[0]

# print(firstLetter("New York"))

# get last letter from string
# def lastLetter(input):
#     return input[-1]

# print(lastLetter("I want some ice cream"))

# get letter at a specified index
# def getIndexLetter(input, index):
#     return input[index]

# print(getIndexLetter("This pizza is tasty!", 8))

# get letters between a specific range

# def getLettersInRange(input, startIndex, endIndex):
#     return input[startIndex:endIndex]

# print(getLettersInRange("I went to New York", 3, 8))

# make string uppercase

# def makeUpperCase(input):
#     return input.upper()

# print(makeUpperCase("I am learning Python!"))

# make string lowercase

# def makeLowerCase(input):
#     return input.lower()

# print(makeLowerCase("London is the capital of the UK"))

# remove whitespace

# def removeWhiteSpace(input):
#     return input.replace(" ", "")

# print(removeWhiteSpace("There are many spaces in ths string"))

# def name(input):
#     return f"Hello, {input}"

# print(name("Tim"))

# basic conditional

# age = 16

# def canGoClubbing():
#     if age >= 18:
#         print("Yes, you can go clubbing!")
#     else:
#         print("Sorry, you can't go clubbing")
    
# canGoClubbing()

# created function to check the length of a string

# def stringLength(input):
#     if len(input) == 5:
#         print("String is 5 characters long!")
#     else:
#         print("String is not 5 characters long!")

# stringLength("abcde")

# fruits = ["apple", "pear", "plum", "strawberries", "oranges"]

# print(fruits)

# add item to a list

cars = ["Lambo", "Ferrari"]

def addItem(existingList, newItem):
    existingList.append(newItem)

    print(cars)

addItem(cars, "Nissan")

def removeCar(car):
    cars.remove(car)
    return cars

print(removeCar("Lambo"))