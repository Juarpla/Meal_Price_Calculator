""""
Student: Juan Plasencia
Showing Creativity:
-Tip percentage added
-"While" expression added in order to be able to receive the correct amount of change, otherwise it will ask for a higher amount again.

"""

#Asking information
child_price = float(input("\nWhat is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
number_child = int(input("How many children are there? "))
number_adult = int(input("How many children are there? "))
tip = float(input("What is the tip percentage? "))
tax = float((input("What is the sales tax rate? ")))


#Obtaining results
subtotal = (child_price * number_child) + (adult_price * number_adult)
subtotal_tip = tip * subtotal / 100
sales_tax = tax * subtotal / 100
total = subtotal + sales_tax + subtotal_tip

#Displaying results
print(f"\nSubtotal: ${subtotal:,.2f} \nTip: ${subtotal_tip:,.2f} \nSales Tax: ${sales_tax:,.2f} \nTotal: ${total:,.2f}")

#Calculating change, if is sufficient
change = 0
transaction = False
while not transaction:
    payment = float(input("\nWhat is the payment amount? "))
    if payment >= total:
        change = payment - total
        print(f"Change: ${change:,.2f}")
        transaction = True
    else:
        print("\nThe payment is insufficient, enter again a higher amount, please.")
#note: "while not" runs as long as a condition is false