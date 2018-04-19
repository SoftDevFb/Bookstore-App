'''
    Author: Frankie Barrios
    Date: 11/27/17
    Purpose: Froggy's Book Store App
'''

books_file = open("bookList.txt", "r")
lines = books_file.readlines()

aryBooks = []
aryChoice = []
aryQty = []

for line in lines:
    line = line.rstrip()
    aryBooks.append(line.split(","))


def menu():
    print("Welcome to Froggy's Book Store!".upper())
    more = "y"
    while (more=="y"):
        print("Here are the books we have:")
        '''for i in range(0,len(aryBooks)):
            print(i+1, aryBooks[i],line.strip())'''

        for book in aryBooks:
            print(book[0],book[1],book[3])

        flag = "y"
        while flag == "y":
            try:
                choice = int(input("Which one would you like?"))
            except ValueError:
                print("Not a number, please choose again.")
                flag == "n"
            else:
                print("Thank you, moving on.")
                break

        flag = "y"
        while flag == "y":
            try:
                qty = int(input("How many would you like?"))
            except ValueError:
                print("Not a number, please choose again.")
                flag == "n"
            else:
                print("Thank you, moving on.")
                break
                
        aryChoice.append(choice)
        aryQty.append(qty)
        more = input("Would you like to add another?").lower()                    


def calculations():    
    salesTax = .076
    for i in range (0,len(aryChoice)):
        choice = aryChoice[i]
        price = (aryBooks[choice][3])
        priceAsFloat = float(price)
        qtyOrdered = (aryQty[i])
        subTotal = priceAsFloat * qtyOrdered
        taxTotal = salesTax * subTotal
        grandTotal = subTotal + taxTotal
        print(grandTotal)
              
def main():           
    menu()
    calculations()
    



main()
