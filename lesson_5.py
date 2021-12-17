# 實戰分析歐洲足球比賽數據

import pandas as pd

 
euro = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/Euro_2012_stats_TEAM.csv',
                  sep=',')    # sep= 表分割用符號

# euro = pd.read_csv('lesson_5.csv', sep= ',')  # 為何不能直接存取檔案??


# DataFram 物件
# 找出文件內所有文件  .dtypes
print(euro.dtypes)

# Team                           object
# Goals                           int64
# Shots on target                 int64
# Shots off target                int64
# Shooting Accuracy              object
# % Goals-to-shots               object
# Total shots (inc. Blocked)      int64
# Hit Woodwork                    int64
# Penalty goals                   int64
# Penalties not scored            int64
# Headed goals                    int64
# Passes                          int64
# Passes completed                int64
# Passing Accuracy               object
# Touches                         int64
# Crosses                         int64
# Dribbles                        int64
# Corners Taken                   int64
# Tackles                         int64
# Clearances                      int64
# Interceptions                   int64
# Clearances off line           float64
# Clean Sheets                    int64
# Blocks                          int64
# Goals conceded                  int64
# Saves made                      int64
# Saves-to-shots ratio           object
# Fouls Won                       int64
# Fouls Conceded                  int64
# Offsides                        int64
# Yellow Cards                    int64
# Red Cards                       int64
# Subs on                         int64
# Subs off                        int64
# Players Used                    int64
# dtype: object

# 搜尋特定欄位資料
cards = euro[['Team', 'Yellow Cards', 'Red Cards']]   # 用中括號[] 選出需要欄位，用','分開  
print(cards)

#                    Team  Yellow Cards  Red Cards
# 0               Croatia             9          0
# 1        Czech Republic             7          0
# 2               Denmark             4          0
# 3               England             5          0
# 4                France             6          0
# 5               Germany             4          0
# 6                Greece             9          1
# 7                 Italy            16          0
# 8           Netherlands             5          0
# 9                Poland             7          1
# 10             Portugal            12          0
# 11  Republic of Ireland             6          1
# 12               Russia             6          0
# 13                Spain            11          0
# 14               Sweden             7          0
# 15              Ukraine             5          0

# 將搜尋資料進行排序  sort_values('欄位名稱', ascending= False(降冪)/True(升冪))
card_1= cards.sort_values('Yellow Cards', ascending= False)
print(card_1)

#                    Team  Yellow Cards  Red Cards
# 7                 Italy            16          0
# 10             Portugal            12          0
# 13                Spain            11          0
# 0               Croatia             9          0
# 6                Greece             9          1
# 1        Czech Republic             7          0
# 9                Poland             7          1
# 14               Sweden             7          0
# 4                France             6          0
# 11  Republic of Ireland             6          1
# 12               Russia             6          0
# 3               England             5          0
# 8           Netherlands             5          0
# 15              Ukraine             5          0
# 2               Denmark             4          0
# 5               Germany             4          0

# Series 物件
# 取得單一欄位資料 
print(euro.Goals) 

# 0      4
# 1      4
# 2      4
# 3      5
# 4      3
# 5     10
# 6      5
# 7      6
# 8      2
# 9      2
# 10     6
# 11     1
# 12     5
# 13    12
# 14     5
# 15     2
# Name: Goals, dtype: int64

# 總分平均分數
print(euro.Goals.mean())
# 4.75

# 四捨五入之平均數  round
print(round(euro.Goals.mean()))
# 5

# 尋找大於分數之團隊   ** 篩選或過濾條件使用[]
print(euro[euro.Goals > 5])

#         Team  Goals  Shots on target  Shots off target  ... Red Cards Subs on  Subs off  Players Used
# 5    Germany     10               32                32  ...         0      15        15            17
# 7      Italy      6               34                45  ...         0      18        18            19
# 10  Portugal      6               22                42  ...         0      14        14            16
# 13     Spain     12               42                33  ...         0      17        17            18

# 尋找資料 ''開頭
s= euro.Team.str.startswith('S')  # 出來結果是bool值  Ture/False
print(s)

# [4 rows x 35 columns]
# 0     False
# 1     False
# 2     False
# 3     False
# 4     False
# 5     False
# 6     False
# 7     False
# 8     False
# 9     False
# 10    False
# 11    False
# 12    False
# 13    False
# 14    False
# 15    False
# Name: Team, dtype: bool

print(euro[s])  # 將"euro.Team.str.startswith('S')"裝入[] 使用DataFram 就會得到以下結果

#       Team  Goals  Shots on target  Shots off target  ... Red Cards Subs on  Subs off  Players Used
# 13   Spain     12               42                33  ...         0      17        17            18
# 14  Sweden      5               17                19  ...         0       9         9            18

# 取部分資料  .iloc (以座標標示)
print(euro.iloc[0:3, 1:4])     # 列位0~3位置  欄位1~4  

#    Goals  Shots on target  Shots off target
# 0      4               13                12
# 1      4               13                18
# 2      4               10                10

# 使用行列名稱取得資料  .loc['索引值', '欄位名稱']
print(euro.loc['0':'3', 'Team':'Hit Woodwork'])

#              Team  Goals  Shots on target  ...  % Goals-to-shots Total shots (inc. Blocked) Hit Woodwork
# 0         Croatia      4               13  ...             16.0%                         32            0
# 1  Czech Republic      4               13  ...             12.9%                         39            0
# 2         Denmark      4               10  ...             20.0%                         27            1
# 3         England      5               11  ...            

