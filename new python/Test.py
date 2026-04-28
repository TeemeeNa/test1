#1.List เหมือน Tuple แต่สามารถเปลี่ยนค่าข้างในได้แต่ tuple เปลี่ยนไม่ได้
import numbers

#names = ["John", "Bob", "Khun", "Nhun"]
#names[0] = "jojo" -> แทนที่ John -> jojo
#print(names[0:3]) #Output = ["jojo", "Bob", "Khun", "Nhun"]


#2.Insert ->นำตัวแปรที่ต้องการ ใส่ลงตำแหน่งด้านหน้าของตัวที่กำหนด
#input = int(input("Enter here"))
#number = [1,2,3,4,5]
#.insert(4, input) ->4 คือตัวแหน่งตัวที่ 5 ของ list
#print(number) #Output = [1, 2, 3, 4, 9, 5]


#3.In ->Check ว่ามี 1 ใน numbers ไหม ถ้ามี =True
#numbers = [1,2,3,4,5]
#print(1 in numbers)


#4.len ดูว่ามี กี่ตัวในตัวแปร numbers
#numbers = [1,2,3,4,5,9]
#print(len(numbers))


#5.for loop ดูค่าแต่ล่ะตัวใน list แล้วปริ้นออกมาตัวล่ะบรรทัด 1 เว้น 2 เว้น 3...9
#numbers = [1,2,3,4,5,9]
#for it in numbers:
    #print(it)


#6.while loop output = 1 เว้น 2 เว้น 3... 9
#i = 0
#numbers = [1,2,3,4,5,9]
#while i < len(numbers):
    #print(numbers[i])
    #i += 1


#7.Range
#numbers = range(5, 10, 2) #->(เริ่ม , จบ, ที่ละเท่าไหร่)
#for number in numbers:
    #print(number) output = 5 7 9



#8.Tuple เหมือน list แต่เปลี่ยนต่าไม่ได้ list = [] ,tuple = ()
#และใช้พวก .append .insert ไม่ได้
#numbers = (1,2,3)

#9.Function กำหนดค่า function และใช้ โดยมี "f" ->print(f"{something}")
#def happy(name, age):
    #print(f"Happy birthday {name}")
    #print(f"you are {age} years old")

#(input(""), int(input("")))

#Example 2
#def display_voice(username, amount,due_date,knife):
    #print(f"Hello {username}")
    #print(f"The amount you have to pay is {amount:.2f}, please pay before {due_date}")
    #print(f"Or else I shove my {knife} up your a$$")

#display_voice(input("Enter your name"), float(input()), input(), input("Enter something to shove up his a$$"))

#Example 3
#def plus(a,b):
    #c = a + b
    #return c
#print(plus(int(input()),int(input())))

#Example 4
#def Create_Name(first,last):
    #first = first.capitalize() #-> ตัวอักษรแรกตัวใหญ่
    #last = last.capitalize()
    #return first + " " + last
#full_name = Create_Name(input("Enter your first name: "),input("Enter your last name: "))
#print(full_name)


#10.Build in function
#x = 3.14
#y = -5
#z = 5
#a = hello
#result = len(a)        #-> 5 ตัวอักษร 5 ตัว
#result = round(x)      #-> 3 ปัดขึ้นลง
#result = abs(y)        #-> 5 ทำให้เป็นบวกเสมอ
#result = pow(z, 3)     #-> 5 ยกกำลัง 3
#result = max(x, y, z)  #-> = 5ตัวอะไรเยอะสุด
#result = min(x, y, z)  #-> =-5ตัวอะไรน้อยสุดสุด
#if a == "0":
    #pass               #-> ข้าม
#print(result)


#11.logical operator -> and or not
#temp = 20
#is_raining = True
#if temp >35 or temp < 0 or is_raining: # -> ขอแค่อย่างใดอย่างนึงเข้าเงื่อนไข
    #print("The outdoor event is cancel")
#else:
    #print("The outdoor event is still scheduled")


#12.conditional expression ใช้ if else ในบรรทัดเดียว
#สูตร X if condition else Y
#num = 5
#print("Positive" if num > 0 else "Negative")


#13.indexing -> ใช้ [] [start : stop : step]
#credit_number = "1234-5678-9012"
#print(credit_number[4]) #-> - เพราะ "-" เป็นตัวที่ 4 0-4
#print(credit_number[:4])    #->"1234" ไม่รวม "-" stop ไม่รวมตัวท้าย
#print(credit_number[5:9])   #->"5678"
#print(credit_number[5:])    #->"5678-9012"
#print(credit_number[-1])    #->"2" นับจากหลังสุด
#print(credit_number[::2])    #->"13-6891" เริ่ม 1 (ไปที่ล่ะ 2)
#print(credit_number[::3])    #->"146-1" เริ่ม 1 (ไปที่ล่ะ 3)


#14.format specifiers
# price1 = 3.14159

#1. จำนวนทศนิยม valuable:.2f = ตัวแปรทศนิยม 2 ตำแหน่ง
#print(f"Price 1 is {price1:.2f}")   #->Price 1 is 3.14

#2. จำนวนตัวอักษรมีกี่ตัว
#print(f"Price 1 is {price1:10}")    #->Price 1 is    3.14159

#3. จำนวนตัวอักษรมีกี่ตัว + 0 อยู่ด้านหน้า
#print(f"Price 1 is {price1:010}")   #->Price 1 is 0003.14159

#4. จำนวนตัวอักษรมีกี่ตัว + space อยู่ด้านหลัง
#print(f"Price 1 is {price1:<10}")   #->Price 1 is 3.14159 space อยู้ด้านหลังแทน

#5. จำนวนตัวอักษรมีกี่ตัว + space อยู่ด้านหน้า
#print(f"Price 1 is {price1:>10}")   #->Price 1 is    3.14159 (เหมือนธรรมดา)

#6. จำนวนตัวอักษรมีกี่ตัว + ตัวแปรอยู่ตรงกลาง
#print(f"Price 1 is {price1:^10}")   #->Price 1 is  3.14159

#7. ตัวแปรที่เป็นบวกจะมี "+" อยู่ด้านหน้า ตัวไหนลบ "-"
#print(f"Price 1 is {price1:+}")     #->Price 1 is +3.14159

#8. ตัวแปรที่เป็นบวกจะมี " " ตัวลบไม่มี
#print(f"Price 1 is {price1: }")     #->Price 1 is  3.14159

# p1 = 9000.1414
#9. ตัวแปรจะมี ","
#print(f"Price 1 is {p1:,}")         #->Price 1 is 9,000.1414

#10. ตัวแปรจะมี ",", ตัวที่ + จะ "+" และ ทศนิยม 2 ตำแหน่ง
#print(f"Price 1 is {p1:+,.2f}")     #->Price 1 is +9,000.14


#15.while loop
#name = input("Enter your name: ")

#while name == "": #-> หากยังเป็น "" จะ print
    #print("You did not enter your name")
    #name = input("Enter your name: ")
#else:
    #print(f"Your name is {name}")

#16.for loop (start stop step)
#1.1 for x in range(1, 11):#เริ่ม 1 -> 10
    #print(x)
#1.2for x in reversed(range(1, 11)):#เริ่ม 10 -> 1
    #print(x)
#1.3 for x in range(1, 11, 3):#เริ่ม 1 -> 4 -> 7 -> 10
    #print(x)

#2.card = "1234-5678-9012-3456"
#for x in card:
    #print(x) #ปริ้นทีล่ะตัว

#3.for x in range(1, 21):
    #if x == 13:
        #continue #ข้าม 13
    #else:
        #print(x)


#17.nested loop (loop ซ้อน loop)
#Ex->Outer loop:
        #inner loop:

#for y in range(3): #->ทำให้ทุก code ที่อยู่ด้านล่างจะทำงาน 3 ครั้ง
    #for x in range(1, 10):
        #print(x, end="") #-> end="" -> คือการทำให้ไม่ขึ้นบรรทัดใหม่
    #print() #-> ขึ้นบรรทัดใหม่

#สร้างสี่เหลี้ยมโดนใช้ nested loop
#rows = int(input("Enter the # of rows: ")) #บรรทัด
#cols = int(input("Enter the # of columns: ")) #ความยาว
#symbol = input("Enter the symbol: ") #ตัวอักษรที่ใช้
#for x in range(rows):
    #for y in range(cols):
        #print(symbol, end="") #-> end="" -> คือการทำให้ไม่ขึ้นบรรทัดใหม่
    #print() #-> ขึ้นบรรทัดใหม่

#18. 2D collections ใน list มีหลาย list ได้
#fruits =        ["apple", "banana", "cherry", "orange"]
#vegetables =    ["celery", 'carrot', "potatoes"]
#meats =         ["chicken", "fish", "turkey"]

#groceries = [fruits, vegetables, meats]
#print(groceries[1][0]) #= "celery" -> vegetable -> celery

#for collection in groceries:
    #for food in collection:
        #print(food, end=" ") #ปริ้นทุกตัวใน list ตั้งแต่ fruits -> meats
    #print()


#19.Dictionary (Dict) -> {key:value}
# capitals = {"USA": "Washington D.C.",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}

#print(capitals.get("USA")) #-> Washington D.C.
#if capitals.get("Japan"):
    #print("That capitals exists")
#else:
    #print("That capitals doesn't exist")
#capitals.update({"Germany": "Berlin"})  #-> เพิ่มเข้าไปใน dict ด้วย
#capitals.update({"USA": "Detroit"})     #->เปลี่ยนจาก Washington D.C. -> Detroit
#capitals.pop("China")                   #-> China หายจาก dict
#capitals.popitem()                      #ลบ ตัวที่มาหลังที่สุดใน dict

#1.keys = capitals.keys()                  #China : Beijing , China = keys
#for key in capitals.keys():
    #print(key)

#2.values = capitals.values()              #China : Beijing, Beijing = values
#for value in capitals.values():
    #print(value)

#3.items = capitals.items()    #([('USA', 'Washington D.C.'), ('India', 'New Delhi'), ('China', 'Beijing')])
#print(items)                # [(), (), ()]

#Example
#items = capitals.items()
#for key, value in capitals.items():
    #print(f"{key}: {value}")

#USA: Washington D.C.
#India: New Delhi
#China: Beijing
#Russia: Moscow


#20.Function (def)
#Example1
# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name}")
#     print(f"You are {age} years old")
#     print(f"Happy Birthday to you")
#     print()
# happy_birthday("Bro", 30)
# happy_birthday("Khun", 20)
# happy_birthday("Nhun", 15)
#
# #Example2
# def display_voice(username, amount,due_date,knife):
#     print(f"Hello {username}")
#     print(f"The amount you have to pay is {amount:.2f}, please pay before {due_date}")
#     print(f"Or else I shove my {knife} up your a$$")
#
# display_voice(input("Enter your name"), float(input()), input(), input("Enter something to shove up his a$$"))

#Example 3
#def plus(a,b):
    #c = a + b
    #return c
#print(plus(int(input()),int(input())))

#Example 4
#def Create_Name(first,last):
    #first = first.capitalize() #-> ตัวอักษรแรกตัวใหญ่
    #last = last.capitalize()
    #return first + " " + last
#full_name = Create_Name(input("Enter your first name: "),input("Enter your last name: "))
#print(full_name)


#21.Keyword argument (1.positional 2.default 3.KEYWORD 4.arbitrary)
#1.positional -> Hello("Hello") fixed ไว้แล้วว่าต้องเป็นอะไร

#2.default    -> def greet(name="Guest):
                #     print("Hello, name")
                # greet() -> Hello guest

#3.keyword    -> hello(first= "Khun") #มีตัวบอกใน argument ว่าตัวนี้คืออะไร
#                print("1", "2", "3" , sep="-") sep = seperate เป็น function build in


#Ex1
# def net_price(list_price, discount= 0, tax = 0.025): #สามารถเขียน ลงใน parameter ได้เลยถ้าคิดว่าไม่มีเปลี่ยน
#     return list_price * (1 - discount) * (1 + tax)
# # print(net_price(500))
# print(net_price(500, 0.1, 0))                        #ในกรณีคนมี discount

#Ex2
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
# hello("Hello", title="Mr.", first="SpongeBob", last="SquarePants")

#Ex3
# def get_phone(country, area, first, last):
#     return f"+{country}-{area}-{first}-{last}"
# phone_num = get_phone(country=66, area=123, first=456, last=7890)
# print(phone_num)


#4.arbitrary  -> *arg = ให้รับค่า argument ได้หลายตัวพร้อมเปลี่ยนตัวเองเป็น Tuple()
#                **kwarg = ให้รับค่า keyword argument หลายค่า พร้อมเปลี่ยนตัวเองเป็น
#                          dict{} {keys:values}
#1.*args
#Ex1 *args
# def add(*args): #-> parameter จะชื่ออะไรก็ได้ Ex *Nums
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4,5,6,7)) #argument
#
# #Ex2 *args
# def display_name(*names):
#     for name in names:
#         print(name, end=" ")
# display_name("Dr.", "SpongeBob", "Harold", "Squarepants")


#2.**kwargs
#Ex1 **kwargs
# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key:6}: {value}")
# print_address(street="123 Fake St.",
#               apt="papaya pok pok apartment",
#               city="New York",
#               state="NY",
#               zip="10600") #-> argument

#Ex2 arg อยู่ก่อน kwarg เสมอ
# def shipping_label(*args, **kwargs): #*args ดู shipping_label("Dr.", "SpongeBob")
#     for arg in args:                 #**kwargs ดู pping_label(zip="10600")
#         print(arg, end=" ")
#     print()
#     # for value in kwargs.values():
#     #     print(value)
#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('pobox')}") #ถ้าไม่มี apartment แต่มี pobox ให้ใส่แทน
#     else:
#         print(f"{kwargs.get('street')}")                       #ถ้าไม่ apartment ไม่ต้องใส่
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
# shipping_label("Dr.", "SpongeBob", "Harold", "Squarepants",
#                street="123 Fake St.",
#                apt="papaya pok pok apartment",
#                city="New York",
#                state="NY",
#                zip="10600",
#                pobox="PO box #1001")