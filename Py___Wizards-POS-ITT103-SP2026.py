#This dictionary store the list of items available, the cost and inventory

items_description = {
    "beer": {"price": 150.00, "stock_count": 10},
    "cupcake": {"price": 90.00, "stock_count": 5},
    "broom": {"price": 800.75, "stock_count": 50},
    "pasta": {"price": 250.20, "stock_count": 15 },
    "soda": {"price": 150.00, "stock_count": 10 },
    "coffee": {"price": 98.50, "stock_count": 12 },
    "towel": {"price": 580.62, "stock_count": 8 },
    "lasco": {"price": 650.96, "stock_count": 7 },
    "cookies": {"price": 480.32, "stock_count": 8 },
    "freshener": {"price": 850.98, "stock_count": 9 },
    "wipes": {"price": 350.00, "stock_count": 25 },
    "napkin": {"price": 250.00, "stock_count": 6 },
    "toothpaste": {"price": 150.00, "stock_count": 16 },
}

#This block of code list the menu of available items, price and stock count to the cashier

print("=== Best Buy Retail Store- Available Item ===\n")
for item in items_description:
    price = items_description[item]["price"]
    stock = items_description[item]["stock_count"]
    print(f"{item.title()}: price ${price:.2f}:| {stock} avail in stock")
print("\n=======================================================\n")

#This outer while loop allows the cashier to conduct multiple transactions in one session

while True:

# An empty dictionary is created to store the items entered by the cashier to the cart facilitating multiple transactions

    cart = {}
    subtotal = 0

#The cashier is prompted to enter the name of the item(s) to be added to the cart. Order is validated as being a part of the available list of items and in stock. Several options are provided: '0' to complete order, 'remove' to remove an item and 'view' to view the cart

    while True:
        order = input("\nPlease enter the name of the item(s) to be added to the cart: ('0' to complete, 'remove' to remove and 'view' to view the cart) ").lower().strip()

#This block of code calculates the subtotal and applicable taxes once the order is complete

        if order == "0":
            print("\nYour order is complete!\n")
            print("==================================")
            for item, quantity in cart.items():
                print(f"Item: {item} x Qty: {quantity} x Unit Price: ${items_description[item]['price']:.2f}")
            print("==================================\n")
            subtotal = sum(items_description[item]["price"] * quantity for item, quantity in cart.items())
            print(f"subtotal: ${subtotal:.2f}")
            discount = 0
            if subtotal > 5000:
                discount = subtotal * 0.05
                print(f"5% discount has been applied- ${discount:.2f}")
                subtotal-=discount

            sales_tax = 0.10
            tax_included = subtotal * sales_tax
            total = subtotal + tax_included
            print(f"total tax: ${tax_included:.2f}")
            print(f"total due: ${total:.2f}\n")
            print("----------------------------------\n")

#This block of code prompts the cashier to accept payment. Payment is validated to ensure the cash tendered is equal to or greater than the total amount due

            while True:
                try:
                    payment_received = float(input("Please enter the amount received: ").strip())
                    if payment_received < total:
                        print("Payment received is less than total. Please enter a larger amount")
                        continue
                    else:
                        change = payment_received - total
                        print(f"Change is ${change:.2f}")

# Company name is stored for receipt generation
                        store_name = "Best Buy Retail Store"

# Thank you message is attached at the end of receipt
                        end_message = "Thank You"

# The receipt is printed from the order completed

                        print(f"\n======== {store_name} ========")
                        print("------------- RECEIPT -------------")
                        for item, quantity in cart.items():
                            print(f"Item: {item} x Quantity: {quantity} x Unit Price: ${items_description[item]['price']:.2f} | Total Price: ${items_description[item]['price'] * quantity:.2f}")
                        print(f"Subtotal: $ {subtotal:.2f}")
                        print(f"Total Tax: $ {tax_included:.2f}")
                        print(f"Payment Received: $ {payment_received:.2f}")
                        print(f"Change: $ {change:.2f}")
                        print("===================================")
                        print(f"             {end_message}\n")

                        break

                except ValueError:
                    print("Please enter a numeric value")
# The cashier is given the option to conduct multiple transactions after checkout is completed

            new_transaction = input("Would you like to start a new transaction? (y/n) ").lower().strip()
            if new_transaction != "y":
                print("Exiting... Goodbye!")
                exit()
            else:
                break

#This block of code is executed if the cashier chooses to remove an item from the cart

        if order == "remove":
            removed_item = input("Please enter the name of the item(s) to be removed from the cart: ").lower().strip()

            if removed_item in cart:
                removed_quantity = int(input("Please enter the quantity of the item(s) to be removed from the cart: "))

                if removed_quantity > cart[removed_item]:
                    print("quantity exceeds what's in the cart")

                else:
                    cart[removed_item] -= removed_quantity
                    items_description[removed_item]["stock_count"] += removed_quantity

                    if cart[removed_item] <= 0:
                        del cart[removed_item]
                    print("Item successfully removed!")

            else:
                print("Item not found in cart!")

#This block is executed to display the cart per the cashier's selection

        elif order == "view":
            if not cart:
                print("Your cart is empty :(")
            else:
                print("\n------ YOUR CART -----")
            for item, quantity in cart.items():
                subtotal = sum(items_description[item]["price"] * quantity for item, quantity in cart.items())
                sales_tax = 0.10
                tax_included = subtotal * sales_tax
                total = subtotal + tax_included
                print(f"Item: {item} x Quantity: {quantity} x Unit Price: ${items_description[item]['price']:.2f}")
            print(f"Total Price: ${items_description[item]['price'] * quantity:.2f}")
            print(f"total tax: ${tax_included:.2f}")
            print(f"total due: ${total:.2f}")

#This block of code is executed when the cashier selects an item to be added to the cart. They are prompted to enter the item quantity which is then validated against available stock.

        if order in items_description:
            try:
                quantity = int(input("Please enter the quantity of the item(s) to be added to the cart: "))
            except ValueError:
                print("Please enter a numeric value")
                continue
            stock_count = items_description[order]["stock_count"]

#Out of stock notification if the quantity in the inventory is zero (0)

            if stock_count == 0:
                print("Out of Stock")

#Qunatity exceeds available stock is executed if the cashier enters a quantity for an item that exceeds what is available in the inventory

            elif quantity > stock_count:
                print("Quantity Exceeds Available Stock")

#This block of code is executed if not of the above conditions are met and the item is in stock

            else:
                print("Your item has been added to the cart")
                items_description[order]["stock_count"] -= quantity

#The block of code is executed after the item is added to the cart wherein the cashier will be notified if the stock count for the item selected falls below five (5)

                if items_description[order]["stock_count"] < 5:
                    print("Low stock alert! Less than 5 items left")

#This block of code enables the cashier to increase the quantity of an item that is already in the cart by entering the name of the item and the quantity to be increased by instead of overwriting the original order

                if order in cart:
                    cart[order] += quantity
                else:
                    cart[order] = quantity

#This is executed if the item entered to be added to the cart is not in the dictionary

        else:
            print("Item not available!")








