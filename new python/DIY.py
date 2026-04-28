#Exercise1
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


#Exercise2 ->guess number
# import random
# computor = random.randint(1,100)
# is_running = True
# total_guess = 0
# player = int(input("Enter number between 1 and 100: "))
# total_guess += 1
# while is_running == True:
#
#     if computor == player and total_guess == 1:
#         print("Magnificent! You got it in the first try.")
#         break
#
#     elif computor == player:
#         print(f"You got it in the {total_guess} tries!")
#         break
#
#     while computor != player:
#         if computor < player:
#             print("It's lower than that!")
#             total_guess += 1
#             player = int(input("Enter number between 1 and 100: "))
#
#         elif computor > player:
#             print("It's higher than that!")
#             total_guess += 1
#             player = int(input("Enter number between 1 and 100: "))


#Exercise3 ->guess number Plus+
# import random
#
# def run():
#     ask = input("Do you want to play again (Y/N): ")
#     if ask.upper() == "Y":
#         return True
#     elif ask.upper() == "N":
#         print("Goodbye")
#         return False
#     else:
#         print("Invalid choice")
#         return run()
#
#
# def diff():
#     print("Welcome to number guess+")
#     print("A = Easy    (1-50, 7 guesses)")
#     print("B = Medium  (1-100, 7 guesses)")
#     print("C = Hard    (1-100, 5 guesses)")
#     return input("Choose your difficulty: ").upper()
#
#
# # 🔹 รองรับ difficulty เพิ่มในอนาคตง่ายมาก
# DIFFICULTY = {
#     "A": {"max": 50, "guess": 7},
#     "B": {"max": 100, "guess": 7},
#     "C": {"max": 100, "guess": 5},
# }
#
# is_running = True
#
# while is_running:
#     difficulty = diff()
#
#     if difficulty not in DIFFICULTY:
#         print("Invalid difficulty\n")
#         continue
#
#     max_num = DIFFICULTY[difficulty]["max"]
#     guess_left = DIFFICULTY[difficulty]["guess"]
#     num = random.randint(1, max_num)
#     total_guess = 0
#
#     print(f"\nGuess a number between 1 and {max_num}")
#
#     while guess_left > 0:
#         player = int(input("Your guess: "))
#         total_guess += 1
#         guess_left -= 1
#
#         if player == num:
#             if total_guess == 1:
#                 print("🎉 Magnificent! First try!")
#             else:
#                 print(f"🎉 You guessed it in {total_guess} guesses!")
#             break
#         elif player < num:
#             print(f"Too low! ({guess_left} guesses left)")
#         else:
#             print(f"Too high! ({guess_left} guesses left)")
#
#     else:
#         print(f"💀 Out of guesses! The number was {num}")
#
#     print()
#     is_running = run()


#Exercise4 Menu
# def menu():
#     print("Hello welcome to menu")
#     print("Press 1: Say hello")
#     print("Press 2: Goodbye")
#     print("Press 0: Exit")
#     choice = input("Enter your choice: ")
#     return choice
# choice = menu()
# if choice == "1":
#     print("Hello")
# elif choice == "2":
#     print("Goodbye")
#     exit()
# elif choice == "0":
#     exit()


#Exercise5 Grading
# stu1 = int(input("Enter 1st student points: "))
# stu2 = int(input("Enter 2nd student points: "))
# stu3 = int(input("Enter 3rd student points: "))
# stu4 = int(input("Enter 4th student points: "))
# stu5 = int(input("Enter 5th student points: "))
# all = [stu1, stu2, stu3, stu4, stu5]
#
# A = (stu1 + stu2 + stu3 + stu4 + stu5)/5
# print(int(A))
# print(max(all))
# print(min(all))

#Exercise6 Even Odd

num = input("Enter a number: ")
num1 = num.isdigit()

while num1:
    if int(num) % 2 == 0:
        print(num, "is even")
        break
    elif int(num) % 2 != 0:
        print(num, "is odd")
        break
else:
    print(num, "is not a number")