# Dictionary
# dictionary是使用key和value為一對, {key1:value1, key2:value2}
# key= 使用不可變動物件(字串/數值/tuple), 但不可使用list
# key值不可重複
# value= 無使用限制

dic_1= {'a':1, 'b':2, 'c':3, 'c': 5}
print(dic_1)

# {'a': 1, 'b': 2, 'c': 5}  重複的key對應value會被覆蓋
#/////////////////////////////////////////////////////

# 取出物件
print(dic_1['a'])

# 1
#////////////////////////////////////////////////////

# 取不存在數值，並給予一個value
print(dic_1.get('d', 'No data'))

# No data
#////////////////////////////////////////////////////

# 使用tuple為key
dic_2 = {(2,3):'A', (5,-3):'B', (-1,-5):'C'}   # 座標
print(dic_2[(5,-3)])

# B
#////////////////////////////////////////////////////

# keys() 取得字典中所有key值 /values() 取得字典中所有value值 / items() 取得字典中所有key值和value值
# 如要一個個取出 可以使用for_loop
print(dic_2.keys()) 
print(dic_2.values())
print(dic_2.items())

#dict_keys([(2, 3), (5, -3), (-1, -5)])
# dict_values(['A', 'B', 'C'])
# dict_items([((2, 3), 'A'), ((5, -3), 'B'), ((-1, -5), 'C')])
#////////////////////////////////////////////////////////

# 新增 /  刪除一個-del, 刪除全部-clear
dic_1['d'] = 4   
print(dic_1)

del dic_1['d']
print(dic_1)

dic_1.clear()
print(dic_1)

# {'a': 1, 'b': 2, 'c': 5, 'd': 4}
# {'a': 1, 'b': 2, 'c': 5}
# {}