import numpy as np
# array = np.array([["A", "B", "C"],
#                   ["X", "Y", "Z"],
#                   ["1", "2", "3"]])
# print(array.ndim)   #ndim ใช้สำหรับบอกจำนวนมิติ 2 dim
# print(array.shape)  #shape ใช้สำหรับบอกขนาดของ [มิติ, แถว, คอลัมน์]- (3,3)

# array = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
#                   [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
#                   [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "_"]]])
# print(array.ndim)   #ndim ใช้สำหรับบอกจำนวนมิติของอาเรย์ 3 dim
# print(array.shape)  #shape ใช้สำหรับบอกขนาดของ [ความลึกAJS, แถวABC DEF GHI, คอลัมน์ ABC]-
# print(array[0, 1, 2])   #F ลึก 0 แถว 1 คอลัมน์ 2 #A ลึก 0 แถว 0 คอลัมน์ 0
# word = array[0,1,0] + array[0,2,2] + array[0,1,1] # D + I + E
# print(word) #DIE


#---SLICING---
array = np.array([[1,2,3,4], 
                   [5,6,7,8], 
                   [9,10,11,12],
                  [13,14,15,16]])
#array[start:end:step]
#row:column
print(array.ndim)
print(array[:, 1::2])