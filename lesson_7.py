
# pandas-- groupby
#分群計算分析方法

import pandas as pd
# 讀取資料
users = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/u.user.txt', sep='|', index_col='user_id')

# 計算分群之平均數  groupby('選擇欄位')
age_avg = users.groupby('occupation').age.mean()
print(age_avg)

# occupation
# administrator    38.746835
# artist           31.392857
# doctor           43.571429
# educator         42.010526
# engineer         36.388060
# entertainment    29.222222
# executive        38.718750
# healthcare       41.562500
# homemaker        32.571429
# lawyer           36.750000
# librarian        40.000000
# marketing        37.615385
# none             26.555556
# other            34.523810
# programmer       33.121212
# retired          63.071429
# salesman         35.666667
# scientist        35.548387
# student          22.081633
# technician       33.148148
# writer           36.311111
# Name: age, dtype: float64

## 分析哪一個職業的男性比率最高
# * 將性別轉為數字
def gender_to_numeric(x):  # x為參數
    if x == 'M':
        return 1  # 若x=M 回傳1
    if x == 'F':
        return 0  # 若x=F 回傳0

# * 函式Apply( )
# 利用DataFram 不需要用for_loop將每筆資料拿出來計算
# 先找出預計算欄位
users['gender'].apply(gender_to_numeric)

# user_id
# 1      1
# 2      0
# 3      1
# 4      1
# 5      0
#       ..
# 939    0
# 940    1
# 941    1
# 942    0
# 943    1
# Name: gender, Length: 943, dtype: int64

# * 計算出每一個職業中男生所佔的比例，並且降冪排序(公式：每一個職業男性數量的總和 ÷ 每一個職業的總數)
# 新增欄位將轉換結果放入
users['gender_n'] = users['gender'].apply(gender_to_numeric)
print(users)
#          age gender     occupation zip_code  gender_n
# user_id
# 1         24      M     technician    85711         1
# 2         53      F          other    94043         0
# 3         23      M         writer    32067         1
# 4         24      M     technician    43537         1
# 5         33      F          other    15213         0
# ...      ...    ...            ...      ...       ...
# 939       26      F        student    33319         0
# 940       32      M  administrator    02215         1
# 941       20      M        student    97229         1
# 942       48      F      librarian    78209         0
# 943       22      M        student    77841         1

### 計算出每一個職業中男生所佔的比例，並且降冪排序
# 公式：每一個職業男性數量的總和 ÷ 每一個職業的總數
result = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100
print(result.sort_values(ascending= False))
# doctor           100.000000
# engineer          97.014925
# technician        96.296296
# retired           92.857143
# programmer        90.909091
# executive         90.625000
# scientist         90.322581
# entertainment     88.888889
# lawyer            83.333333
# salesman          75.000000
# educator          72.631579
# student           69.387755
# other             65.714286
# marketing         61.538462
# writer            57.777778
# none              55.555556
# administrator     54.430380
# artist            53.571429
# librarian         43.137255
# healthcare        31.250000
# homemaker         14.285714
# dtype: float64