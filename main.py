import time
import re

menu = ["Black Coffee", "Espresso", "Latte", "Cappuccino", "Frappuccino"]

print("Hello, Welcome to Python Barista.\nWhat can I get started for you?\nHere is our menu for today:\n" + "\n".join(menu))  # Join menu items with newline

time.sleep(5)

print("What would you like to order?")
order_input = input().title()

# Check if any menu item is a substring of the order input
matched_items = [item for item in menu if item.lower() in order_input.lower()]

if matched_items:
    order = matched_items[0]  # Take the first matched item
    print("Great! " + order + " is a great choice.\nJust one for today?")
    answer = input().lower()
    if answer.startswith("yes"):
        print("Great!\nCan I please have a name for the order?")
        name = input()
        print("Thank you, " + name + ", I'll get started on that order for you.")
        time.sleep(5)
        print("Here is your " + order + ". Enjoy!")
    elif answer.startswith("no"):
        # Check for quantity in the response
        quantity_match = re.search(r'\d+', answer)
        if quantity_match:
            qty = quantity_match.group()
            print("Got it! I'll prepare " + qty + " " + order + "(s) for you.")
            time.sleep(5)
            print("Here are your " + qty + " " + order + "(s). Enjoy!")
        else:
            print("I'm sorry, I didn't understand your response.")
else:
    print("I'm sorry, that item is not on our menu.")
