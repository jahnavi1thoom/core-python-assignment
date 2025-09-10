def add(initial_menu, add_item):
    initial_menu.append(add_item)

def removet(initial_menu, remove_item):
    if remove_item in initial_menu:
        initial_menu.remove(remove_item)
    else:
        print(f'Item "{remove_item}" not found in menu!')

def check(initial_menu, check_item):
    if check_item in initial_menu:
        print(f'Availability: "{check_item} is available"')
    else:
        print(f'Availability: "{check_item} is not available"')
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
add(initial_menu, add_item)
removet(initial_menu, remove_item)
initial_menu = [item.capitalize() for item in initial_menu]
formatted_menu = '[' + ', '.join(f'"{item}"' for item in initial_menu) + ']'
print("Updated menu:", formatted_menu)
check(initial_menu, check_item)
