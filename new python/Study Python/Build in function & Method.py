#Build in function
x = 3.14
y = -5
z = 5
a = "hello"
#result = len(a)        #-> 5 ตัวอักษร 5 ตัว
#result = round(x)      #-> 3 ปัดขึ้นลง
#result = round(x, 1)   #-> 3 ปัดขึ้นลง ทศนิยม 1 ตัว
#result = abs(y)        #-> 5 ทำให้เป็นบวกเสมอ
#result = pow(z, 3)     #-> 5 ยกกำลัง 3
#result = max(x, y, z)  #-> = 5ตัวอะไรเยอะสุด
#result = min(x, y, z)  #-> =-5ตัวอะไรน้อยสุดสุด
#if a == "0":
    #pass               #-> ข้าม
#break = ออกจาก loop
#print(result)


#Methods ถ้าอยากรู้เพิ่มพิม print(help(str))
name = "teeMee"
digit = 123
phone = "094-498-9411"
#result = name.find("m")        #-> 3 หาตัวอักษรที่กำหนด เริ่มจาก 0
#result = name.rfind("e")       #-> 5 หาตัวอักษรตัวสุดท้าย ถ้าไม่มีขึ้น -1
#result = name.capitalize()     #-> TeeMee ตัวอักษรแรกตัวใหญ่
#result = name.upper()          #-> TEEMEE ตัวอักษรทั้งหมดใหญ่
#result = name.lower()          #-> teemee ตัวอักษรทั้งหมดเล็ก
#result = name.isdigit()        #-> False ถ้าเป็นตัวเลขทั้งหมดถึงจะ True
#result = digit.is_integer()       #-> True เพราะมีแต่ตัวเลข
#result = name.isalpha()        #-> True เพราะมีแต่ตัวอักษร (ไม่รวมเว้นวรรค)
#result = digit.isalpha()       #-> False เพราะมีตัวเลข (ไม่รวมเว้นวรรค)
#result = phone.count("-")      #-> 3 เพราะมี - -ตัวในตัวแปร
#phone = phone.replace("-", "") #-> phone จะเป็น 0944989411
#print(result)

#format specifiers
#price1 = 3.14159

#1. จำนวนทศนิยม valuable:.2f = ตัวแปรทศนิยม 2 ตำแหน่ง
#print(f"Price 1 is {price1:.2f}")   #->Price 1 is 3.14

#2. จำนวนตัวอักษรมีกี่ตัว
#print(f"Price 1 is {price1:10}")    #->Price 1 is    3.14159

#3. จำนวนตัวอักษรมีกี่ตัว + 0 อยู่ด้านหน้า
#print(f"Price 1 is {price1:010}")   #->Price 1 is 0003.14159

#4. จำนวนตัวอักษรมีกี่ตัว + space อยู่ด้านหลัง
#(f"Price 1 is {price1:<10}")   #->Price 1 is 3.14159 space อยู้ด้านหลังแทน

#5. จำนวนตัวอักษรมีกี่ตัว + space อยู่ด้านหน้า
#(f"Price 1 is {price1:>10}")   #->Price 1 is    3.14159 (เหมือนธรรมดา)

#6. จำนวนตัวอักษรมีกี่ตัว + ตัวแปรอยู่ตรงกลาง
#print(f"Price 1 is {price1:^10}")   #->Price 1 is  3.14159

#7. ตัวแปรที่เป็นบวกจะมี "+" อยู่ด้านหน้า ตัวไหนลบ "-"
#print(f"Price 1 is {price1:+}")     #->Price 1 is +3.14159

#8. ตัวแปรที่เป็นบวกจะมี " " ตัวลบไม่มี
#print(f"Price 1 is {price1: }")     #->Price 1 is  3.14159

#p1 = 9000.1414
#9. ตัวแปรจะมี ","
#(f"Price 1 is {p1:,}")         #->Price 1 is 9,000.1414

#10. ตัวแปรจะมี ",", ตัวที่ + จะ "+" และ ทศนิยม 2 ตำแหน่ง
#print(f"Price 1 is {p1:+,.2f}")     #->Price 1 is +9,000.14


#collection = ตัวเก็บค่าตัวแปร
#List = []เปลี่ยนตัวด้านในได้ สร้างซ้ำได้
#Set = {}
#Tuple = ()

#1.List[] มีตัวซ้ำได้
fruits = ["apple", "orange", "banana", "coconut"]
#print(fruits[0]) # apple
#print(fruits[1]) # orange
#print(fruits[:3]) #["apple", "orange", "banana"]
#print(fruits[::2]) #['apple', 'banana']
#print(fruits[::-1]) #['coconut', 'banana', 'orange', 'apple']
#print("apple" in fruits)  # True
#fruits[0] = "pineapple" #apple -> pineapple

#FUNCTION
#print(len(fruits))             # 4
#fruits.append("pineapple")     # pineapple ต่อท้าย
#fruits.remove("apple")         # ลบ apple
#fruits.insert(0, "pineapple")  # (ตำแหน่ง, คำที่อยากเพิ่ม)
#fruits.sort()                  # จัดคำตาม a-z
#fruits.reverse()               # ย้อนหลัง
#fruits.clear()                 #ใน fruits = ""
#print(fruits.index("apple"))   #ค้นหาตำแหน่งของ apple
#print(fruits.index("orange"))  #ค้นหาตำแหน่งของ orange
#print(fruits.count("apple"))    #1 เพราะมีคำว่า apple แค่ 1 ตัว


#2.Set{} ไม่เรียงลำดับ(สุ่ม) เพิ่มลดตัวใน set ได้ แต่มีตัวซ้ำไม่ได้

#FUNCTION
# fruits = {"apple", "orange", "banana", "coconut"} #ห้ามมี apple มากกว่า 1 ตัว
# fruits.add("pineapple")    # ใส่ได้ใน set แต่ไม่เรียง
# fruits.pop()               #ลบตัวด้านหน้าสุด
# print(fruits)


#3.Tuple() เรียงลำดับแต่ เปลี่ยนเพิ่มลดตัวใน tuple ไม่ได้ แต่มีตัวซ้ำได้
#fruits = ("apple", "orange", "banana", "coconut", "coconut")