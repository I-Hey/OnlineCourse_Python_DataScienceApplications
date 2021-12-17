# 課堂練習

import pandas as pd
chipo = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/chipotle.tsv',
                   sep='\t')

# 確認欄位資料型態
print(chipo.dtypes)
# order_id               int64
# quantity               int64
# item_name             object
# choice_description    object
# item_price            object
# dtype: object

# 轉換型態   str > float
# 先將欄位內容取出
for value in chipo.item_price:
    print(value)
# $6.49
# $16.98
# $17.98
# $16.98
# $16.98
# $8.99
# $8.99
# $8.49

# 將符號移除
# $為字串索引值0的位置
for value in chipo.item_price:
    print(value[1:])
# 8.99
# 8.49
# 9.25
# 8.75
# 2.95
# 11.48
# 2.39

price = [float(value[1:]) for value in chipo.item_price]    # 由str轉為float
chipo.item_price = price
   # 將price傳給 chipo物件中的item_price
print(chipo.dtypes)

# order_id                int64
# quantity                int64
# item_name              object
# choice_description     object
# item_price            float64
# dtype: object