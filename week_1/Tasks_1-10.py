#Task 1
print("#Task 2")
print("Hours in a week:")
print(7*24)
print("Minutes in a week:")
print(7*24*60)
print("Seconds in a week:")
print(7*24*60*60)
print("")

#Task 2
print("#Task 2")
name = input("What is your name?")
mail = input("What is your email address?")
nickname = input("What is your nickname?")
print("")
print("##Let's review your information##")
print(f"Your name: {name}")
print(f"Your email address: {mail}")
print(f"Your nickname: {nickname}")
print("")
print(f"{name} | {mail} | {nickname}")
print("")

#Task 3
print("#Task 3")
name = input("What is your name? ")
victim = input("Who is your victim? ")
print(f"Name: {name}")
print(f"Victim: {victim}")
print("Thank you, " + name + "!")
print("But our " + victim + " is in another castle!")
print("")

#Task 4
print("#Task 4")
name = "Courier"
age = 34
city ="New Vegas"
print(f"Hi {name}, you are {age} years old. You live in {city}.")
print("")

#Task 5
print("#Task 5")
name = "Ozan Akyol"
age = 18
skill1 = "python"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000
print(f"My name is {name}, I am {age} years old")
print("")
print("My skills are")
print(f"- {skill1} {level2}")
print(f"- {skill2} {level2}")
print("")
print(f"My salary expectation is {lower}-{upper} euros/month")
print("")

#Task 6
print("#Task 6")
number1 = 3
number2 = 5
print(f"number1 is: {number1}")
print(f"number2 is: {number2}")
print("")
print(f"{number1} + {number2} = {number1+number2}")
print(f"{number1} - {number2} = {number1-number2}")
print(f"{number1} * {number2} = {number1*number2}")
print(f"{number1} / {number2} = {number1/number2}")
print("")

#Task 7
print("#Task 7")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight/((height*height)/10000)
print(f"Your BMI is {BMI}")
print("")

#Task 8
print("#Task 8")
gamename = input("Enter a game name: ")
gamerelased = input("Which year was this game released? ")
print("")
print(f"{gamename} is {2025-int(gamerelased)} years old.")
print("")

#Task 9
print("#Task 9")
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1*number2*number3
print(f"The product is {product}")
print("")

#Task 10
print("#Task 10")
weakly_eat_cafe = float(input("How many times a week do you eat at the student cafeteria? "))
price_luch = float(input("The price of a typical student lunch? "))
spend_groceries = float(input("How much money do you spend on groceries in a week? "))
print("")
print("Average food expenditure: ")
daily_lunch = float(price_luch*(weakly_eat_cafe/7)) 
daily_groceries = float(spend_groceries/7)
print(f"Daily: {daily_lunch+daily_groceries} liras")
print(f"Weekly: {daily_lunch*7+daily_groceries*7} liras")
print(f"Monthly: {(daily_lunch+daily_groceries)*30} liras")