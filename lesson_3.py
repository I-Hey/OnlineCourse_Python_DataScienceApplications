# Numpy- python套件/ 處理多維度資料

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
print(list_1, list_2)

import numpy as np 


np_1 = np.array(list_1)   # array 陣列，type要一致
np_2 = np.array(list_2)
print(np_1)
# [1 2 3 4]

# 確認資料型態 .dype
print(np_1.dtype)
# int32  type= int/ 32位元

# 轉變型態 .astype
tmp = np_1.astype(np.float64)
print(tmp.dtype)
# float64  type= float/ 64位元


# 陣列運算 / 可以進行 + - * /
print(np_1 * 2)
print(np_1 * np_2)
print(np_1 + np_2)
print(np_1 / np_2)
print(np_1 - 2)

# [2 4 6 8]
# [ 5 12 21 32]
# [ 6  8 10 12]
# [0.2        0.33333333 0.42857143 0.5       ]
# [-1  0  1  2]

# 陣列中取出數值/ 
print(np_1[1])  #[數值位置]
print(np_1[1 : 3])  # 位置1~3 但不包含位置3
print(np_1[1 :])
print(np_1[-1])  
# 2
# [2 3]  
# [2 3 4]

# 重新定義新的數值
np_1[0] = 18  # 0位置改為18
print(np_1)
# [18  2  3  4]

# 一維陣列改為二維陣列
np_1 = np_1.reshape(2,2)
print(np_1)
# [[18  2] [ 3  4]]
np_2 = np_2.reshape(2, 2)
print(np_2)
# [[5 6] [7 8]]

# 矩陣相乘  .doc
print(np_1.dot(np_2))
# [[104 124] [ 43  50]]