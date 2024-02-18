# Create a tuple of the 18 elements
elements = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

# Create a list to store the menu items
menu_items = []

# Loop through the tuple and add the elements to the list
for element in elements:
    if element % 3 == 0:
        menu_items.append("ONE: {}  ".format(element).ljust(10))
    elif element % 3 == 1:
        menu_items.append("TWO: {}  ".format(element).ljust(10))
    else:
        menu_items.append("THREE: {}  ".format(element).ljust(10))

# Print the menu
print("  ___________________    ____________________    ____________________ ")
print("|      ONE            ||          TWO         ||        THREE         |")
print("|=====================||======================||======================|")
for menu_item in menu_items:
    print(menu_item)
