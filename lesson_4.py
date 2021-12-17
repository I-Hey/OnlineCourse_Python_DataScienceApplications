# pandas- python分析套件

import pandas as pd

# 匯入資料(網址)/csv方式 / 檔案也可以
users = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/u.user.txt',
                   sep='|',
                   index_col='user_id')    # sep= 檔案所使用分隔符號 /  定義索引欄位




# 列印前五筆資料  .head
print(users.head())
#          age gender  occupation zip_code
# user_id
# 1         24      M  technician    85711
# 2         53      F       other    94043
# 3         23      M      writer    32067
# 4         24      M  technician    43537
# 5         33      F       other    15213

# 列印後五筆資料  .tail
print(users.tail())
#         age gender     occupation zip_code
# user_id
# 939       26      F        student    33319
# 940       32      M  administrator    02215
# 941       20      M        student    97229
# 942       48      F      librarian    78209
# 943       22      M        student    77841

# 如果將 index_col移除
#    user_id  age gender  occupation zip_code
# 0        1   24      M  technician    85711
# 1        2   53      F       other    94043
# 2        3   23      M      writer    32067
# 3        4   24      M  technician    43537
# 4        5   33      F       other    15213

#      user_id  age gender     occupation zip_code
# 938      939   26      F        student    33319
# 939      940   32      M  administrator    02215
# 940      941   20      M        student    97229
# 941      942   48      F      librarian    78209
# 942      943   22      M        student    77841

# 查詢資料總筆數
print(users.shape[0])    # [0] 為資料中的第一個元素
# 943  --總比數

# 查詢資料欄位數
print(users.shape[1])     # [1] 為資料中第二個元素
# 4

# 查詢資料欄位名稱與資料型態  .dtype
print(users.dtypes)
# age            int64
# gender        object
# occupation    object
# zip_code      object
# dtype: object

# 取得特定欄位資料  
print(users.occupation)    # or  users["occupation"]

# user_id
# 1         technician
# 2              other
# 3             writer
# 4         technician
# 5              other
#            ...
# 939          student
# 940    administrator
# 941          student
# 942        librarian
# 943          student
# Name: occupation, Length: 943, dtype: object

# 列印職業欄中特定資料
print(users.occupation[1])    # []內填入第幾筆資料
# technician

# 特定欄位中有多少筆不同的資料
print(users.occupation.nunique())
# 21

# 計算資料的統計數量  ualue_counts
print(users.occupation.value_counts())   # occupation--特定欄位
# student          196
# other            105
# educator          95
# administrator     79
# engineer          67
# programmer        66
# librarian         51
# writer            45
# executive         32
# scientist         31
# artist            28
# technician        27
# marketing         26
# entertainment     18
# healthcare        16
# retired           14
# lawyer            12
# salesman          12
# none               9
# homemaker          7
# doctor             7

# 取出資料中出現次數最多者
print(users.occupation.value_counts().head(1))  # head() 前五筆資料 
# student    196
# Name: occupation, dtype: int64

# 資料中出現次數最少者
print(users.occupation.value_counts().tail(1))
# doctor    7

# 基本統計資料   describe() only計算int資料
print(users.describe())
#               age
# count  943.000000
# mean    34.051962
# std     12.192740
# min      7.000000
# 25%     25.000000
# 50%     31.000000
# 75%     43.000000
# max     73.000000

# 全部欄位統計資料    inculde 加入統計資料型態
print(users.describe(include='all'))  
#                age gender occupation zip_code
# count   943.000000    943        943      943
# unique         NaN      2         21      795
# top            NaN      M    student    55414
# freq           NaN    670        196        9
# mean     34.051962    NaN        NaN      NaN
# std      12.192740    NaN        NaN      NaN
# min       7.000000    NaN        NaN      NaN
# 25%      25.000000    NaN        NaN      NaN
# 50%      31.000000    NaN        NaN      NaN
# 75%      43.000000    NaN        NaN      NaN
# max      73.000000    NaN        NaN      NaN  
