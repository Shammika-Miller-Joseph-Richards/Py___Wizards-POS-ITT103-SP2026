# Py___Wizards-POS-ITT103-SP2026
POS System- Python 

Authors: Joseph Richards and Shammika Miller 
Date Created: Sunday, April 5th, 2026
Course: ITT103- Programming Techniques
GitHub Public URL to code: 
https://github.com/Joseph-sham/Py__Wizards-POS-ITT103-SP2026
https://github.com/Shammika-Miller-Joseph-Richards/Py___Wizards-POS-ITT103-SP2026


Purpose of the program: 

This program is a POS system designed to allow the cashier to add items from a defined menu to the cart for checkout. This design not only allows the cashier to add but also to view the cart and remove items from the cart and accept payment from the customer. 

A unique feature of this program is the ability to automatically update the inventory once an item is added or removed. There are also inventory alerts when an item is 'out of stock', 'less than five (5) items in inventory' and when the cashier enters a 'quantity that exceeds the available stock'.

Payments are validated and the cashier can only enter a value that is equal to or greater that the total due. A detailed receipt is generated upon completion listing the items purchased, unit cost, the subtotal, applicable taxes, discount where applicable (on order exceeding $5,000.00), the total due/received and change returned. 

The program is formatted to prevent non-numerical values of quantity or payments to be entered. 

Multiple transactions can be conducted in a single session wherein the cashier is prompted to make a decision after checkout and payment. 


How to run it:

The menu will be displayed as illustrated here: 

--- Best Buy Retail Store- Available Items ---

xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock
xxx: price $xxx:| x avail in stock


2. You will be prompted to enter the name of the item to be added to the cart, 'remove' gives the option to remove an item while view allows the cashier to view the cart. Please note: the user will not have the option to view the cart before item(s) are added; a message 'Your cart is empty :(' will be displayed prompting the user to add items. 

3. Once an item is selected, it is validated as being a part of the menu, in stock or exceeding the available stock. After which you will prompted be to enter the quantity of the item to be added to the cart. 

4. The item is added to the cart once it is in stock and validated as being a part of the menu.

5. To complete the order select '0'. The checkout process will be initiated.

6. The completed order will be displayed, along with the applicable taxes and total due. 

7. Payment is prompted. The amount entered is validated as being equal to the total amount due or greater than the amount due which presents the remaining balance as change.

8. The receipt is automatically generated with the information from the order including payment received, discounts (if applicable) and change.

9. You have now successfully completed checkout! You now have the option to start a new transaction by entering 'y' or 'n' to exit the POS system. 



Limitations: 

It operates only through a command-line interface without a graphical user interface which might limit user experience.

If the user enters '0' before adding an item the system will recognize it as order completed and prompt for payment. The only way to exit is to enter payment received as zero which generates a blank receipt. prompting a decision to start a new transaction.


Modification: 

The stocks are stored using a dictionary structure.

2. The POS system automatically updates stock when items are added or removed.

3. A low stock alerts are displayed when items fall below five in quantity.

4. its Input validation ensures only correct values are accepted.

5. A clean detailed receipt is generated after each transaction.




