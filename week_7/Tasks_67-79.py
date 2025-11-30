#Task 67
def coordinator(x, y):
    my_tuple = (x, y)
    return my_tuple
my_coord = coordinator(5, 6)
print(my_coord)

#Task 68
my_coordinates = {}

def coordinator(x, y):
    my_tuple = (x, y)
    return my_tuple

my_coordinates[coordinator(0,0)] = "Home"
my_coordinates[coordinator(1,1)] = "Work"
my_coordinates[coordinator(-1,-1)] = "School"

for k,v in my_coordinates.items():
    print(f"position: {k} name: {v}")

#Task 69
def print_best_weapon(weapon_list: list):
    best_melee = max(weapon_list, key= lambda w: w[1])
    print(best_melee[0])

weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]
print_best_weapon(meele_weapon)

#Task 70
game_table = [["_","_","_"],["_","_","_"],["_","_","_"]]
user_inputs = []

print("_ _ _")
print("_ _ _")
print("_ _ _")

def create_tuple_user_input():
    row = int(input("Please enter x: "))
    colmn = int(input("Please enter y: "))
    return (row, colmn)

my_Flag = True
while my_Flag:
    command = input("please type new or exit: ")
    if command.lower() == "exit":
        for(r,c) in user_inputs:
            game_table[r][c] = "*"
        for row in game_table:
            print(row)
        my_Flag = False
    else:
        tup = create_tuple_user_input()
        user_inputs.append(tup)


#Task 71
user_elements = set()

my_Flag = True
while my_Flag:
    item = input("Enter an element for set: ")
    if item.lower() == "exit":
        my_Flag = False
    else:
        user_elements.add(item)

for e in user_elements:
    print(e)

#Task 72
user_elements = set()

my_Flag = True
while my_Flag:
    item = input("Enter an element for set: ")
    if item.lower() == "exit":
        my_Flag = False
    elif item in user_elements:
        print("{item} is already in our set.")
    else:
        user_elements.add(item)

for e in user_elements:
    print(e)

#Task 74
"""
in this code:
"""
"""
>def ask_name():
 > my_ans = ""
 > return input("Please enter a character from Lord of the Rings")
 >
 >def ask_age():
 > my_ans = int(input(f"How old are {name}: "))
 > return my_ans
 >
 >real_age = 55000
 >name = ask_name()
 >question = f"Here is the questions about {name}"
 >print("")
 >user_guess = ask_age()
 >if real_age == user_guess:
 > my_ans = "You’re Right"
 > print(my_ans)
 >else:
 > print("Nope") 
"""

local_variables_list = ["my_ans[inside] --> ask_name()" , "my_ans[inside] --> ask_age()"]
global_variables_list = ["real_age" , "name" , "question" , "user_guess" , "my_ans"]

print("")
print("LOCAL VARIABLES")
print("---------------")
for i in local_variables_list:
    print(i)

print("")
print("GLOBAL VARIABLES")
print("----------------")
for i in global_variables_list:
    print(i)
print("")

#Task 75
def start_game():
    score = 10
    print(f"Game started! Current score: {score}")
    return score

def increase_score(score):
    score += 5
    print(f"Score increased! Current score: {score}")
    return score

def display_score(score):
    print(f"Final score: {score}")

score = 0
score = start_game()
score = increase_score(score)
display_score(score)

#Task 76
def age_calc():
    my_flag = True
    while my_flag:
        try:
            birthyear = int(input("What is your birthday? "))
            current_year = 2025
            age = current_year - birthyear
            return age
        except ValueError:
            print("Invalid Input.")

print(f"You are {age_calc()} years old.")

#Task 77
x = int(input("Please enter a number: "))
flag = True

while flag:
    try:
        y = int(input("Please enter divider: "))
        print(f"{x} divided by {y} is {x / y}")
        flag = False
    except ZeroDivisionError:
        print("You can't enter 0 as divider")
    except ValueError:
        print("Invalid Value")
    except Exception:
        print("Some kind of error occurred")