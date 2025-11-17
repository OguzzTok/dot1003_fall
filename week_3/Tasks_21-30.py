#Task 21
user_input = input("Please input an argument: ")
def my_message(first_arg):
    print(f"Hello {first_arg}")
my_message(user_input)

#Task 22
user_input = input("Please input an argument: ")
def my_message(first_arg):
    return f"Hello {first_arg}"
print(my_message(user_input))

#Task 23
def sum(a, b):
    return a + b
print(sum(12, 2))

#Task 24
name = "Gordon Freeman"
def greeting(input_name):
    print(f"Hi {name}")
greeting("Andrew Ryan")
greeting("Gordon Freeman")

#Task 25
def arth(a, b, c):
    return (a+b+c) / 3
print(arth(3,2,1))

#Task 26
my_name = "Heisenberg"

my_flag = True

while my_flag:
    user_input = str(input("Say my name: "))
    if user_input == my_name:
        print("You're goddamn right.")
        my_flag = False

#Task 27
password = input("Enter your password: ")

my_flag = True

while my_flag:
    again_psw = input("Enter again: ")
    if again_psw == password:
        print("Your password matches and account created successfully")
        my_flag = False
    else:
        print("They are not same.")
my_flag = False

#Task 28
user_number = int(input("Please enter a number: "))

while user_number >0:
    print(user_number)
    user_number -= 1
print("Kaboom")

#Task 29
password = "123"
attempt = 0

my_flag = True

while my_flag == True and attempt<3:
    user_password = input("Password: ")
    if user_password == password:
        print("Welcome")
        my_flag = False
    else:
        print("Try Again.")
        attempt += 1
    if attempt >= 3:
        print("Incorrect Password. Exterminate...”")

#Task 30
print("dumb calculator v0.1 If you want to exit+ enter 0")
total_number = 0
sum = 0
odd = 0
even = 0

my_flag = True

while my_flag:
    my_input = int(input("Please enter a number: "))
    if my_input != 0:
        total_number = total_number+1
        sum = sum+my_input
        if my_input%2 == 0:
            even = even+1
        else:
            odd = odd+1
    else:
        my_flag = False

print(f"Total number: {total_number}")
print(f"Sum: {sum}")
print(f"Mean: {sum/total_number}")
print(f"Odd: {odd} Even: {even}")