#1.import math
#x = 9.1

#print(math.pi)         # pi
#print(math.e)          #
#result = math.sqrt(x)  #square root
#result = math.ceil(x)  # = 10 ปัดทศนิยมขึ้นเสมอ
#result = math.floor(x) # = 9 ปัดทศนิยมลงเสมอ
#print(math.factorial(5)) # = 5*4*3*2*1 = 120
#print(result)


#2.import time
#my_time = int(input("Enter the time in seconds: "))

#1.for x in range(0, my_time):
    #print(x) #-> นับเวลาตามวิ
    #time.sleep(1) #-> พักทีล่ะกี้่วิ

#2.for x in range(my_time, 0, -1): #reverse
    #print(x) #-> นับเวลาตามวิ
    #time.sleep(1) #-> พักทีล่ะกี้่วิ
#print("Hello World")

#3.count down timer
#for x in range(my_time, 0, -1): #reverse
    #seconds = x % 60
    #minutes = int(x/60) %60
    #hours = int(x / 3600)
    #print(f"{hours:02}:{minutes:02}:{seconds:02}") #-> นับเวลาตามวิ
    #time.sleep(1) #-> พักทีล่ะกี้่วิ
#print("Hello World")


#3.import random (สุ่มตัวเลข)
#import random
#number = random.randint(1, 6) #-> สุ่มตั้งแต่ 1 -> 6
#print(number)

#low = 1
#high = 100
#options = ("rock", "paper", "scissors")
#cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(low, high) #-> สุ่มตั้งแต่ 1-100 แต่เป็นจำนวนเต็ม
#number = random.random()           #-> สุ่ม 1-100 แต่รวม float ด้วย
#option = random.choice(options)    #-> สุ่ม rock paper scissors
#random.shuffle(cards)              #->['7', 'K', '8', '6', '10', 'J', '5', '9', '4', '3', '2', 'Q', 'A']