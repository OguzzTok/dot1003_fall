#Task 40
city_name = str(input("Which city: "))
repetition = int(input("How many repetition for 'li': "))

sonuc = city_name + "li" * repetition
print(sonuc + "lerle")

#Task 41
first_word = str(input("First word: "))
second_word = str(input("Second word: "))

if len(first_word) > len(second_word):
    print(first_word)
elif len(second_word) > len(first_word):
    print(second_word)
else:
    print("Their lenght are same")

#Task 42
user_input = str(input("Your Input: "))
print(f"*{user_input}*")

#Task 43
user_input = str(input("Your Input: "))
print(user_input)
print("-" *len(user_input))

#Task 44
user_input = input("Your input: ")
max_lenght = 18

if len(user_input) > max_lenght:
    print("Max input lenght would be 18.")

total_padding = max_lenght - len(user_input)
left_padding = total_padding // 2
right_padding = total_padding - left_padding

output = (">" * left_padding) + user_input + ("<" * right_padding)

print("-" * max_lenght)
print("|" + output + "|")
print("-" * max_lenght)

#Task 45
user_str = input("Please enter string: ")
first_int = int(input("Please enter first integer: "))
second_int = int(input("Please enter second integer: "))

output = user_str[first_int:second_int]

print(output)

#Task 46
user_input = str(input("Please enter string: "))
user_int = int(input("Please enter integer: "))
output = user_input[:user_int]
print(output)

#Task 47
user_input = str(input("Please enter string: "))
user_int = int(input("Please enter integer: "))
output = user_input[user_int:]
print(output)

#Task 48
user_str = input("Please enter string: ")

if "a" in user_str:
    print("found")
else:
    print("not found")

#Task 49
user_str = input("Please enter string: ")
user_item = input("Please enter search item: ")

if user_item in user_str:
    print("found")
else:
    print("not found")

#Task 50
user_input = str(input("Please enter string: "))
item = str(input("Please enret search item: "))

if item in user_input:
    print(f"found it at {user_input.find(item)}")
else:
    print("not found")

#Task 51
my_sentence = "The quick brown fox jumps over the lazy dog"
my_flag = True

while my_flag:
    user_search = str(input("What are you looking for? "))
    if user_search in my_sentence:
        print(f"found it at {my_sentence.find(user_search)}")
    elif user_search == "-1":
        my_flag = False
        print("Bye.")
    else:
        print("not found")

#Task 52
my_list = [1.2345, 2.3456, 3.4567, 4.5678]

def to_two_decimal(numbers):
    string_list = [f"{num:.2f}" for num in numbers]
    float_list = [float(num) for num in string_list]
    return float_list

new_list = to_two_decimal(my_list)
print(new_list)