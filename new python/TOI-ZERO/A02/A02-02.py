import sys

# 1. รับจำนวนจุด
n_input = sys.stdin.readline()
if not n_input:
    exit()
n = int(n_input)

# 2. เตรียมที่เก็บข้อมูล (เราจะแยกกลุ่มตามแนวทแยง)
# เราจะเก็บค่า x ต่ำสุด และ x สูงสุด ของแต่ละกลุ่มไว้
groups_minus = {} # สำหรับพวก x - y
groups_plus = {}  # สำหรับพวก x + y

for i in range(n):
    # อ่านพิกัด x และ y
    line = sys.stdin.readline().split()
    if not line: break
    x = int(line[0])
    y = int(line[1])
    
    # --- จัดกลุ่มแบบ x - y ---
    key_minus = x - y
    if key_minus not in groups_minus:
        # ถ้ายังไม่เคยมีกลุ่มนี้ ให้สร้างใหม่ [x_ต่ำสุด, x_สูงสุด]
        groups_minus[key_minus] = [x, x]
    else:
        # ถ้ามีกลุ่มนี้แล้ว ให้ลองอัปเดตค่าต่ำสุด/สูงสุด
        if x < groups_minus[key_minus][0]: groups_minus[key_minus][0] = x
        if x > groups_minus[key_minus][1]: groups_minus[key_minus][1] = x
        
    # --- จัดกลุ่มแบบ x + y ---
    key_plus = x + y
    if key_plus not in groups_plus:
        groups_plus[key_plus] = [x, x]
    else:
        if x < groups_plus[key_plus][0]: groups_plus[key_plus][0] = x
        if x > groups_plus[key_plus][1]: groups_plus[key_plus][1] = x

# 3. หาขนาดเต็นท์ที่ใหญ่ที่สุด
max_size = 0

# ดูในทุกๆ กลุ่มที่เราแยกไว้
for key in groups_minus:
    x_min, x_max = groups_minus[key]
    side = x_max - x_min # ความยาวด้าน = x ตัวมากสุด ลบ x ตัวน้อยสุด
    if side > max_size:
        max_size = side

for key in groups_plus:
    x_min, x_max = groups_plus[key]
    side = x_max - x_min
    if side > max_size:
        max_size = side

# 4. แสดงคำตอบ
print(max_size)