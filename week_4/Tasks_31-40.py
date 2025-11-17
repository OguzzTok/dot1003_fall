#Task 31
my_list = [3,5,8]
print(my_list)
print(f"My first item: {my_list[0]}")
print(f"List length is {len(my_list)}")
my_list.pop(1)
print(my_list)

#Task 32
my_list = [3,5,8]
print(my_list)
my_list[2] = 50
print(my_list)

#Task 33
my_list = []
user_input = ""

my_flag = True

while my_flag:
    user_input = input("Please enter an input: ")
    if user_input != "exit":
        my_list.append(user_input)
    else:
        print(my_list)
        my_flag = False

#Task 34
my_list = []
user_input = ""

while user_input != "exit":
    user_input = input("Please enter an input: ")
    if user_input != "exit":
        my_list.append(user_input)

for i in my_list:
    print(i)

#Task 35
name = str(input("Please enter an input: "))
for i in name:
    print(f">{i}")

#Task 36
raw_points = [1,2,1,3]
total_points = 0

for i in raw_points:
    total_points += i

print(f"total {total_points} points earned.")

#Task 37
raw_points = [1,-2,1,3,-5,7,0]
total_points = 0

for point in raw_points:
    if point > 0:
        total_points += point

print(f"total {total_points} points earned.")

#Task 38
size = int(input("Please input table size: "))

for i in {size}:
    print("|_" * size + "|")

#Task 39
height = int(input("Spruce height: "))

for i in range(1, height + 1):
    space = " " * (height - i)
    star = "*" * (2 * i - 1)
    print(space + star)

print(" " * (height - 1) + "*")

#Task 40
city_name = str(input("Which city: "))
repetition = int(input("How many repetition for 'li': "))

sonuc = city_name + "li" * repetition
print(sonuc + "lerle")