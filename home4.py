import numpy as np

menu_items = {
    'Col1': {'Option 1': 'John', 'Option 2': 'Marie' , 'Option 3': 'Ben'},
    'Col2': {'Option 4': 'Mike', 'Option 5': 'Sally' , 'Option 6': 'Pual'},
    'Col3': {'Option 7': 'Pete', 'Option 8': 'Chrissy' , 'Option 9': 'Oscar'}
  }




menu_items_array = np.array(menu_items)
transposed_menu_items = np.transpose(menu_items)
print(transposed_menu_items)
