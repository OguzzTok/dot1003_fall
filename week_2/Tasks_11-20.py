#Task 11
fahrenheit = int(input("Please type in a temperature (F)"))
celsius = (fahrenheit-32)* 5/9
print(f"{fahrenheit} degrees fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here")
print("")

#Task 12
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = input("Day of the week: ")
if day_of_the_week == "sunday" or "Sunday":
    hourly_wage *= 2
daily_wages = hourly_wage*hours_worked
print(f"Daily wages: {daily_wages} liras")
print("")

#Task 13
age = int(input("How old are you?: "))
if age <18:
    print("You can't play Dark Souls")
elif 18 <= age < 44:
    print("Here is Dark Souls. Lol")
elif 44 <= age:
    print("You are too old for this sh*t")
print("")

#Task 14
num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
if num1 > num2:
    print(f"First one is greater ({num1} > {num2})")
elif num1 < num2:
    print(f"Second one is greater ({num1} < {num2})")
elif num1 == num2:
    print(f"These are equal ({num1} = {num2})")
print("")

#Task 15
word1 = str(input("Type the first number: "))
word2 = str(input("Type the second one: "))
if word1 > word2:
    print(f"{word2} comes alphabetically last")
elif word1 < word2:
    print(f"{word1} comes alphabetically last")
elif word1 == word2:
    print("These are same!")
print("")

#Task 16
com = str(input("Which community do you belong to?: "))
if com == "New California Republic":
    print("You’re belong to Fallout Universe.")
elif com == "NCR":
    print("You’re belong to Fallout Universe.")
elif com == "Brotherhood of Steel":
    print("You’re belong to Fallout Universe.")
elif com == "Caesar's Legion":
    print("You’re belong to Fallout Universe.")
elif com == "Great Khans":
    print("You’re belong to Fallout Universe.")
elif com == "Vault Dweller":
    print("You’re belong to Fallout Universe.")
else:
    print("Nope, you are not belong to Fallout Lore")
print("")

#Task 17
point = int(input("How many points [0-100]: "))
if point == 0:
    print("you what?") 
elif 0 < point <= 49:
    print("fail")
elif 50<= point <= 59:
    print("1")
elif 60 <= point <= 69:
    print("2")
elif 70 <= point <= 79:
    print("3")
elif 80 <= point <= 89:
    print("4")
elif 90 <= point <= 99:
    print("5")
elif point <= 100:
    print("impossible!")
print("")

#Task 18
number = int(input("Enter number: "))
if number%3 == 0 and number%5 != 0:
    print("Fizz")
elif number%3 != 0 and number%5 == 0:
    print("Buzz")
elif number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
print("")

#Task 19
number = int(input("Please type in a number: "))
if number > 0:
    if number%2 == 0:
        print("The number is even")
    elif number%2 != 0:
        print("The number is odd")
elif number <= 0:
    print("The number is negative or zero")
print("")


#Task 20
year = int(input("Please type in a year: "))
if year%400 == 0: 
    print("That year is leap year.")
elif year%100 == 0:
    print("That year is not leap year.")
elif year%4 == 0:
    print("That year is leap year.")
else:
    print("That year is not leap year.")
print("")