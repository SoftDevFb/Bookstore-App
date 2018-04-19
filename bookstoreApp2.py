'''
    Author: Frankie Barrios
    Date: 11/17/17
    Purpose: Bookstore Point of Sale Application
'''
#INTRO
print("Welcome to Froggy's Bookstore!")
name = input("What is your name? ")

#BOOK ARRAY/LIST
bookList = [["1","Where The Red Fern Grows", "Dog Story", 5.99],
            ["2", "Cat In The Hat", "Cat Stpry", 4.95]]

#BOOK LIST INTRODUCTION
print("Hello", name, ", here are the books we have: ")
for book in bookList:
    print(book[0] + " - " + str(book[1]))

'''BOOK CHOICE, need to link item code to title and display title after choice made!
Also need to include quantity option and display quantity then link
quantity to be able to use to figure totals at end!'''

flag = "y"

while flag == "y":
    choice = int(input("Please enter the item code for the book you'd like: "))
    quantity = int(input("How many would you like? "))
    flag = input("Would you like another book? ")
#print("Ok, here is what's in your basket:\n " + quantity + choice)
#Enter for loop in here somehow to create option if "no".














