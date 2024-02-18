import os
# Create a tuple of the 18 elements
elements = ("start instance", " ", " ", "Initialiaze remote command",
            " ", " ", "shutdown", " ", " "  )
function_names = elements
# Create a list to store the menu items
menu_items = []


os.system('clear')
# Print the menu
print(" ________________________  ________________________  ________________________")
print("|  i-033182bde833796cb   ||                        ||                        |")
print("|========================||========================||========================|")

# Loop through the tuple and add the elements to the list
# = 3 - (len(elements) % 3)
columns = 3
total_rows = len(elements)
remaining_rows = (total_rows % columns)

for i in range(0, total_rows - remaining_rows, columns):
    menunum = i + 1

    # Calculate the width of each column
    column_width = 2
    center_width = 2
    # str.ljust(width[, fillchar])
    # Format the elements in each column
    menu_items.append(" {:<3} {:19.19}".format(str(menunum).ljust(2, " "), str(
        elements[i]).ljust(19, " ")))
    
    menu_items.append(" {:<3} {:19.19}".format(
        str(menunum + 1).ljust(2, " "), str(elements[i + 1]).ljust(19, " ")))
    
    menu_items.append(" {:<3} {:19.19}".format(
        str(menunum + 2).ljust(2, " "), str(elements[i + 2]).ljust(19, " ")))

    # Print the row
    print("|{}||{}||{}|".format(*menu_items))
    menu_items = []

# If there are one or two items in the last row, print them in a single column
if remaining_rows == 1:
    print("| {:<3} {:19.19}||                        ||                        |".format(str(menunum + 1).ljust(2, " "), str(
        elements[total_rows - 1]).ljust(12, " ").center(column_width, " ")))
elif remaining_rows == 2:
    print("| {:<3} {:19.19}|| {:<3} {:19.19}||                        |".format(str(menunum + 2).rjust(2, " "), str(
        elements[total_rows - 2]).ljust(19, " "), str(menunum + 1).ljust(2, " "), str(elements[total_rows - 1]).ljust(19, " ")))
print("|============================================================================|")
print("|=====================         0 to exit           ==========================|")
print("|============================================================================|")

if __name__ == '__main__':
    while (True):
        
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
           function_names[0]()
           # os.system('clear')
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 0:
            os.system('clear')
            print('Thanks')
            os.system('clear')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
