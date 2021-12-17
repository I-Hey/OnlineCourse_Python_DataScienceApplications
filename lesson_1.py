list_1 = [3, 1, 5, 4, 2]
 
# 取出清單內物件
print (list_1[: 3])   #第3位置前之所有物件
print (list_1[2 :])   #第2位置後之所有物件

# [3, 1, 5]
# [5, 4, 2]
#////////////////////////////////////////////////////////////////////////

# 加入物件 append() and extend()
# append.()  加入一個物件
# extend.()  加入多個物件 but要先設定一個小list
list_2= [6, 3]
list_1.append(list_2)
print(list_1)
list_1.extend(list_2)
print(list_1)

# [3, 1, 5, 4, 2, [6, 3]]
# [3, 1, 5, 4, 2, [6, 3], 6, 3]
#/////////////////////////////////////////

# 移除物件 pop() and remove()
list_1.pop(2)  # 移除地2位置物件
list_1.remove(4) # 移除物件'4'
print(list_1)
print(list_1)

# [3, 1, 2, [6, 3], 6, 3]
# [3, 1, 2, [6, 3], 6, 3]
#/////////////////////////////////////////////

# 物件排序  reverse() 物件順序反轉 and sort() 物件資料升冪與降冪排序
list_3= [3, 1, 5, 2, 4]
list_3.reverse()  # 將物件順序反轉
print(list_3)
list_3.sort(reverse= True)   # reverse= False/升冪  reverse= True/降冪
print (list_3)

#[4, 2, 5, 1, 3]
#[5, 4, 3, 2, 1]
#///////////////////////////////////////////////

# Tuple 使用小括弧()將資料包起來, Tuple中的內容不可變動, 不可插入或刪除物件
tuple = (3, 1, 5, 2, 4)   
list_4= list(tuple)   # 將tuple物件轉為list物件

#////////////////////////////////////////////////

# in() 確認資料是否存在，len()表長度，conunt()表數量  / list和tuple都可使用
print(6 in tuple) 
print(len(list_3))
print(len(tuple))
print(list_3.count(3))
print(list_4.count(2))

# False
# 5
# 5
# 1
# 1
