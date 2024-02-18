def print_table(menu_items):
  """Prints a table of the given dictionary.

  Args:
    menu_items: A dictionary of dictionaries.
  """
  # Get the number of columns in the table.
  num_columns = len(menu_items)
  print('there are colums in the table')
  # Create a header row for the table.
  column_names = list(menu_items.keys())

  #print(header_row)
  #for col in column_names:
  #  print(col)
    
  # Print the header row.
  # print(" ".join(column_names))
  # col_counter = num_columns - 1
  # Print each row of the table.
 
  #for column in column_names:
  #  print(column)
  #  print(menu_items[column]['Option 1'])
  
  for i in menu_items:
  # display
    print(menu_items[i].values(), menu_items[i].keys())

     
  #  for rows in menu_items[cols]
  #    print(" ".join(rows))

if __name__ == "__main__":
  # Create a dictionary of dictionaries.
  menu_items = {
    'Col1': {'Option 1': 'John', 'Option 2': 'Marie' , 'Option 3': 'Ben'},
    'Col2': {'Option 4': 'Mike', 'Option 5': 'Sally' , 'Option 6': 'Pual'},
    'Col3': {'Option 7': 'Pete', 'Option 8': 'Chrissy' , 'Option 9': 'Oscar'}
  }

  # Print the table.
  print_table(menu_items)
