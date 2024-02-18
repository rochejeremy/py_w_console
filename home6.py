import json
import os
from collections import defaultdict

os.system('clear')




# Create a list to store the menu items
menu = []

# Read the JSON file
with open('menu.json') as f:
    data = json.load(f)


menu_items = defaultdict(int)




# Iterate over the data and add the menu items to the dictionary
border_char = "#"
border_width = 24
border = border_char * border_width
print(border)
the_name = "John"
the_age = 38

for item, options in data.items():
     item_name = item
     heading = "#{fname:^22}#".format(fname = item_name)
     print(heading)
     #menu[int(item[int])] = item['link']
     for option_num in options:
        print(option_num)
     print(border)
     
