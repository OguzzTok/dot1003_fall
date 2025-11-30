#Task 53
def spruce():
    height = int(input("Spruce height: "))
    box_size = int(input("Box Size: "))

    if box_size < height:
        print("Error: Box size must be greater than or equal to spruce height.")
        return

    print("-" * box_size)

    print("|" + " " * (box_size - 2) + "|")

    for i in range(height):
        stars = "*" * (2 * i + 1)
        padding = (box_size - 2 - len(stars)) // 2
        line = "|" + " " * padding + stars + " " * (box_size - 2 - padding - len(stars)) + "|"
        print(line)

    trunk = "*"
    padding = (box_size - 2 - len(trunk)) // 2
    trunk_line = "|" + " " * padding + trunk + " " * (box_size - 2 - padding - len(trunk)) + "|"
    print(trunk_line)

    print("-" * box_size)

spruce()

#Task 54
my_sentence = "The quick brown fox jumps over the lazy dog"
user_input = input("Which item do you want to search? ")
count = my_sentence.count(user_input)
print(f"item {user_input} appeared {count} times")

#Task 55
def searching_machine():
    user_input = input("Enter the input to search")
    user_search = input("Which item do you want to search? ")

    if "," in user_input:
        data = [x.strip() for x in user_input.split(",")]
    else:
        data = user_input
    
    count = 0

#Task 56
def clear_vowels(user_inp):
    vowels = "aeiouAEIOU"
    result = ""
    for char in user_inp:
        if char not in vowels:
            result += char
    print(result)

my_flag = True

while my_flag:
    user_input = input("Enter text: ")
    clear_vowels(user_input)
    if user_input == "0":
        print("Bye!")
        my_flag = False

#Task 58
game_list = []

def anarya(game_list):
    return game_list[::-1]

my_Flag = True

while my_Flag:
    user_input = input("Please type a game: ")
    if user_input != "exit":
        game_list.append(user_input)
    else:
        print(game_list)
        print(anarya(game_list))
        my_Flag = False

#Task 59
game_list = ["Doom", "Max Payne", "FTL"]

def longest_name(game_list):
    return max(game_list, key=len)

print(game_list)
print(longest_name(game_list))

#Task 60
def finder(my_matrix, element):
    for i, row in enumerate(my_matrix):
        for j, val in enumerate(row):
            if val == element:
                print(f"find at Row: {i}, Column: {j}")
                return True
    return False

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input("Irem to search: "))

for row in my_matrix:
    print(row)

print(finder(my_matrix, element))

#Task 61
def sum_of_row(list_arg, element_arg):
    sum = 0
    for colmn in list_arg[element_arg]:
        sum = sum + colmn
    return sum

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
element = int(input("row no: "))
print(sum_of_row(my_matrix, element))

#Task 62
def sum_of_row(list_arg, element_arg):
    sum = 0
    for row in range(len(list_arg)):
        for colmn in range(len(list_arg[row])):
            if (colmn == element_arg):
                sum = sum + list_arg[row][colmn]
    return sum

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
element = int(input("colmn no: "))
print(sum_of_row(my_matrix, element))

#Task 63
def tripler(list):
    return[x * 3 for x in list]
my_lucky_numbers = [4, 8, 15, 16, 23, 42]
tripled_numbers = tripler(my_lucky_numbers)

print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")

#Task 64
inventory = {}

inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5

for key, value in inventory.items():
    print(f"{key}: {value}")

#Task 65
inventory = {}

inventory["item1"] = 3
inventory["item2"] = 1
inventory["item3"] = 5

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

add_item("item1", 5)
add_item("item4", 1)
add_item("item5", 4)

print("Inventory after updates:")
for key in inventory:
    print(f"{key}: {inventory[key]}")

#Taks 66
inventory = {"item1": 3, "item2": 1, "item3": 5}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] < 0:
            inventory[item] = 0

add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

print("Inventory after updates:")
for key in inventory:
    print(f"{key}: {inventory[key]}")
