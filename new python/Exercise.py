#Exercise1
#สร้าง Story โดย filling in the blank(random)
#adjective1 = input("Enter your adjective: ")
#adjective2 = input("Enter your adjective: ")
#verb1 = input("Enter your verb: ")
#verb2 = input("Enter your verb: ")

#print(f"Today I went to a {adjective1} zoo.") # = print(f"Today I went to a " + adjective1 + " zoo.")
#print(f"It was a {adjective2} zoo.")
#print(f"But I {verb1} because it make me {verb2}")


#Exercise2
#friends = 0
# friends = friends + 1
#friends += 1
#print(friends)


#Exercise3 หาเส้นรอบวงกลม 2*pi*R
#import math
#radius = float(input("Enter the radius of a circle"))
#C = 2 * math.pi * radius
#print(f"The circumference is {round(C, 2)} cm")# -> ปัดเหลือ 2 ทศนิยม
#Output xx.xx cm


#Exercise4 หาพื้นที่วงกลม
#import math
#R = int(input("Enter the radius: "))
#All = math.pi * pow(R, 2)
#print(f"The area of this circle is {round(All, 2)}")


#Exercise5 หาพีทาโกรัส
#import math
#A = int(input("Enter A: "))
#B = int(input("Enter B: "))
# = math.sqrt(pow(A, 2) + pow(B, 2))
#print(f"C = {C}")


#Exercise6 ทำบัตร credit อายุ 18+
#age = int(input("Enter your age: "))
#if age >= 100:
    #print("You are too old")
#elif age >= 18:
    #print("You're now signed up!")
#elif age < 0:
    #print("You haven't born yet")
#else:
    #print("You're too young")


#Exercise7 would you like some food (y/n)
#response = input("Would you like some food? (Y/N)")
#if response.lower() == "y":
    #print("Here you go!")
#elif response.lower() == "n":
    #print("OK, maybe next time!")
#else:
    #print("Sorry, I didn't understand you.")


#Exercise8 ชื่อเต็ม
#first = input("Enter your first name: ")
#last = input("Enter your last name: ")
#if first == "":
    #print("You have to enter your first name. Please try again.")
    #exit()
#elif first == "":
    #print("You have to enter your last name. Please try again.")
    #exit()
#print(f"{first.capitalize()} {last.capitalize()} is your full name.")

#Exercise9
#for_sale = False
#if for_sale:
    #print("This item is for sale")
#elif not for_sale:
    #print("This item is not for sale")


#Exercise10 Calculator
#operator = input("Enter your operator (+ - * /) ")
#num1 = float(input("Enter your first number: "))
#num2 = float(input("Enter your second number: "))

#if operator == "+":
    #print(num1 + num2)
#elif operator == "-":
    #print(num1 - num2)
#elif operator == "*":
    #print(num1 * num2)
#elif operator == "/":
    #print(num1 / num2)
#else:
    #print("Sorry, This is not a valid operator. Please try again.")


#Exercise11 kg -> lbs
#weight = float(input("Enter your weight: "))
#unit = input("Enter your unit (K or L): ")
#if unit == "K":
    #weight = weight * 2.205
    #unit = "Lbs"
    #print(f"Your weight is: {round(weight, 1)} {unit}")
#elif unit == "L":
    #unit = "Kgs"
    #print(f"Your weight is: {round(weight / 2.205, 1)} {unit}")
#else:
    #print(f"{unit} is not a valid unit")


#Exercise12 สภาพอากาศ
#temp = 20
#is_raining = True
#if temp >35 or temp < 0 or is_raining: # -> ขอแค่อย่างใดอย่างนึงเข้าเงื่อนไข
    #print("The outdoor event is cancel")
#else:
    #print("The outdoor event is still scheduled")


#Exercise13 คู่หรือคี่ใช้ if else ใน 1 บรรทัด
#num = 6 #ข้อ 1
#print("Even" if num % 2 == 0 else "Odd")

#a = 6
#b = 7
#max = a if a > b else b
#print(max)


#Exercise14 ชื่อที่ถูกต้อง (function)
#1. username is no more than 12 characters
#2. username must not contain space
#3. username must not contain digits

#username = input("enter your username: ")
#username.find(" ")

#if len(username) >12:
    #print("Your username is too long")
#elif not username.find(" ") == -1:
    #print("Your username can't contain spaces")
#elif username.isalpha() == False:
    #print("Your username can't contain digits")
#else:
    #print(f"Welcome {username}")


#Exercise15 อยากได้ 4 ตัวสุดท้ายของตัวแปร (indexing [])
#credit_num = "1234-5678-9012-3456"
#lastfour = credit_num[-4:]
#print(f"XXXX-XXXX-XXXX-{lastfour}")


#Exercise16 reverse number (indexing [])
#credit_num = "1234-5678-9012-3456"
#credit_num = credit_num[::-1]
#print(credit_num) #-> 6543-2109-8765-4321


#Exercise17 while loop ใส่ age ที่ถูกต้อง
#age = int(input("Enter your age: "))
#while age == "":
    #print("You have to fill in your age")
    #age = int(input("Enter your age: "))
#while age < 0:
    #print("Age can't be negative")
    #age = int(input("Enter your age: "))
#print(f"Your age is {age} years old")


#Exercise18 food you like (q = quit)
#food = input("What food do you like? (q to quit): ")
#while not food == "q":
    #print(f"You like {food}")
    #food = input("What another food do you like? (q to quit): ")
#else:
    #print("Bye")

#
#num = int(input("Enter a number between 1 and 10: "))
#while num < 1 or num > 10:
    #print(f"{num} is not between 1 and 10")
    #num = int(input("Enter a number between 1 and 10: "))
#else:
    #print(f"You picked {num}")


#Exercise19 Interest rate (ดอกเบี้ย) calculator
#principle = 0 # -> เงินลงทุน
#rate = 0 # -> อัตรา
#time = 0

#while principle <= 0:
    #principle = float(input("Enter the principle amount:"))
    #if principle <= 0:
        #print("Principle amount cannot be less or equal to zero")
    #else:
        #break

#while rate <= 0:
    #rate = float(input("Enter the interest rate:"))
    #if rate <= 0:
        #print("Interest rate cannot be less or equal to zero")

#while time <= 0:
    #time = int(input("Enter the time in years:"))
    #if time <= 0:
        #print("Time cannot be less or equal to zero")

#total = principle * pow((1 + rate/100), time) # -> สูตรหาดอกเบี้ย

#print(f"Your toal balance after {time} years is {total:.2f} bahts")


#Exercise20 count down timer (import time)

#for x in range(my_time, 0, -1): #reverse
    #seconds = x % 60
    #minutes = int(x/60) %60
    #hours = int(x / 3600)
    #print(f"{hours:02}:{minutes:02}:{seconds:02}") #-> นับเวลาตามวิ
    #time.sleep(1) #-> พักทีล่ะกี้่วิ
#print("Hello World")


#Exercise21 Shopping cart(list set tuple)

#foods = []
#prices = []
#total = 0

#while True:
    #food = input("Enter a food to buy (q to quit):")
    #if food.lower() == "q":
        #break
    #else:
        #price = float(input(f"Enter the price of {food}:"))
        #foods.append(food)
        #prices.append(price)
#print("----- YOUR CART -----")
#for food in foods:
    #print(food, end=" ")
#print("")
#print("")
#print("----- TOTAL -----")
#for price in prices
    #total += price :#(total = total + price)
#print(f"Your total is: {total}")


#Exercise22 สร้าง num_pad (ใช้ 2D List)
#num_pad = ((1, 2, 3),
           #(4, 5, 6),
           #(7, 8, 9),
           #("*", 0, "#"))
#for row in num_pad:
    #for num in row: #nested loop
        #print(num, end=" ")
    #print("")


#Exercise23 Python quiz game
#questions = ("How many elements are in the periodic table?: ",
            #"What is 2+1 = ?: ",
            #"Can you brush your teeth with a truck?: ",
           # "How many bones are in human body?: ",
           # "Which planet are we live in?: ") # tuple เพราะเปลี่ยนไม่ได้
#options = (("A.116", "B.117", "C.118", "D.119"),
           #("A.3 ", "B.4", "C.5", "D.7"),
           #("A.Yes ", "B.No", "C.Maybe", "D.I'm gay"),
           #("A.206", "B.207", "C.208", "D.404"),
           #("A.Earth ", "B.Mars", "C.Blackhole", "D.Sun"))

# = ("C", "A", "B", "A", "A")
#guesses = []
#score = 0
#question_num = 0
#for question in questions:
    #print("-------------")
    #print(question)
    #for option in options[question_num]:
        #print(option)

    #guess = input("Enter (A,B,C,D):").upper()
    #guesses.append(guess)
    #if guess == answers[question_num]:
        #score += 1
        #print("Correct!")
    #else:
        #print("Incorrect!")
        #print(f"{answers[question_num]} is the right answer")
    #question_num += 1

#print("answers: ", end ="")
#for answer in answers:
    #print(answer, end=" ")

#print("guesses: ", end ="")
#for guess in guesses:
    #print(guess, end=" ")
#print(f"Your total score is {score}")


#Exercise23 Menu
#menu = {"pizza": 3.00,
        #"nacho": 4.50,
        #"popcorn": 6.00,
        #"fries": 2.50,
        #"chips": 1.00,
        #"pretzel": 3.50,
        #"soda": 3.00,
        #"lemonade": 4.25}
#cart = []
#total = 0
#print("-------- MENU ---------")
#for key, value in menu.items():
    #print(f"{key:10}: {value:.2f}")
#print("-----------------")
#while True:
    #food = input("Select an item (q to quit): ")
    #if food.lower() == "q":
        #break
    #elif menu.get(food) is not None: # ถ้าใน menu ไม่ใช่ None ให้นำอาหารใส่ cart แต่ถ้า None ไม่ใส่
        #cart.append(food)

#print("-------- ORDER ---------")
#for food in cart:
    #total += menu.get(food)
    #print(food, end=" ")

#print()
#print(f"Total: {total:.2f}")


#Exercise24 เกมเดาเลข
#import random
#num = random.randint(1, 100)
#total_guess = 0
#is_running = True

#while is_running:
    #guess = input("Guess a number between 1 and 100: ")
    #if guess.isdigit():
        #guess = int(guess)
        #total_guess += 1
        #if guess < 1 or guess > 100:
            #print("That number is out of range")
            #print("Guess a number between 1 and 100")
        #elif guess < num:
            #print("It's too low")

        #elif guess > num:
            #print("It's too high")

        #elif guess == num:
            #print("Good Jobs! It's correct")
            #total_guess += 1
            #break

#percentage = 1/total_guess * 100
#print(f"Your total guess is {total_guess}")
#print(f"Which is {percentage}%")


#Exercise25 Rock paper Scissor ทำเอง
# import random
# option = ["rock", "paper", "scissor"]
# player = None
# computor = random.choice(option)
#
# inp = input("Rock, Paper, Scissor? ").lower()
# print(f"Your choice is {inp}")
# print(f"Computer choice is {computor}")
#
# while inp not in option:
#     print("Invalid answer")
#     inp = input("Rock, Paper, Scissor? ")
#
# if inp.lower() == "rock" and computor == "paper":
#     print("You lose!")
#     exit()
# elif inp.lower() == "rock" and computor == "scissor":
#     print("You win!")
#     exit()
# elif inp.lower() == "paper" and computor == "rock":
#     print("You win!")
#     exit()
# elif inp.lower()== "paper" and computor == "scissor":
#     print("You lose!")
#     exit()
# elif inp.lower() == "scissor" and computor == "paper":
#     print("You win!")
#     exit()
# elif inp.lower() == "scissor" and computor == "rock":
#     print("You lose!")
#     exit()
# while inp.lower() == computor:
#     print("It's a tie! Try again!")
#     computor = random.choice(option)
#     inp = input("Rock, Paper, Scissor? ").lower()
#     print(f"Your choice is {inp}")
#     print(f"Computer choice is {computor}")
#
#     if inp.lower() == "rock" and computor == "paper":
#         print("You lose!")
#         exit()
#     elif inp.lower() == "rock" and computor == "scissor":
#         print("You win!")
#         exit()
#     elif inp.lower() == "paper" and computor == "rock":
#         print("You win!")
#         exit()
#     elif inp.lower()== "paper" and computor == "scissor":
#         print("You lose!")
#         exit()
#     elif inp.lower() == "scissor" and computor == "paper":
#         print("You win!")
#         exit()
#     elif inp.lower() == "scissor" and computor == "rock":
#         print("You lose!")
#         exit()