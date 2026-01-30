'''
1. Coffee Shop Ordering System (Basic) 
Scenario: 
You are developing a simple ordering system for a new coffee shop. The system needs to calculate the total bill for a customer's order and apply a discount if applicable.  
Task: 
Create a Python program that performs the following actions: 
Display a menu with item names and prices (e.g., Coffee: $3.50, Muffin: $2.00, Bagel: $4.00). 
Prompt the user to select items and quantities. 
Calculate the total cost of the order. 
Apply a 10% discount if the total bill exceeds $20.00. 
Display the final amount payable.  

2.Scenario: You are processing credit card numbers (e.g., "4532111188885678"). 
Task: Write a function that: 
Takes the string as input. 
Returns a "masked" version where all digits except the last 4 are replaced by * (e.g., "************5678"). 
Focus: Function definitions, string slicing, and the * repetition operator.
'''
#coffee shop ordering system
while(True):
    print("here is your menu :\n 1.coffee:$3.50 \n 2.Muffin:$2.00 \n 3.Bagel :$4.00 \n4.Exit")
    total=0
    choice=int(input("enter your menu order items(1,2 and 3):"))
    if choice==4:
        break
    qty=int(input("       enter the quantity of the item :"))
    if choice==1:
        total=3.50*qty
    elif choice==2:
        total=2.00*qty
    elif choice==3:
        total=4.00*qty
    else:
        print("Invalid item, Kindly enter the menu items...")
    print("Original price:",total)
    discount=0
    if total>20:
        discount=total-total*0.1
        print("After 10% dicount the actual price is : ",discount)
    #payment

    numbers=str(input("Enter the credit card numbers : "))
    print("length",len(numbers))
    star='*'*(len(numbers)-4)
    print("marked number :",star+numbers[-4:])

#paindrome string and numbers
a=int(input("enter the palindrome number:"))
b=a
rev=0
while a>0:
    c=a%10
    rev=rev*10+c
    a//=10
if rev==b:
    print("it is palindrome")
else:
    print("it is not a palindrome")

a=input("enter the palindrome string:")
rev=""
b=a
for i in a:
    rev=i+rev
    print(rev)
if rev==b:
    print("it is palindrome")
else:
    print("it is not a palindrome")

        
