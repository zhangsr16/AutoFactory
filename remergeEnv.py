# avgArea = [1]
# sumArea = [0, 2, 3, 4]
# avgField = [1, 3, 5]
# sumField = [0, 2, 4]
avgSummary = [5, 6, 7, 9]
sumSummary = [2, 3, 4]
nowSummary = [0, 1, 8]

# avgType = [1]
# sumType = [0, 2, 3]
# avgETF = [3, 4, 5, 15, 16, 19]
# sumETF = [0, 2, 6, 9, 10, 17, 18, 20, 21, 22]
# nowETF = [1, 7, 8, 11Fst, 12Fst, 13MAX, 14MIN]

import pandas as pd

# 示例数据
data1 = {
    'Max': [1, 3, 5, 7, 9],
    'OtherColumn': [10, 20, 30, 40, 50]
}

data2 = {
    'Max': [2, 2, 6, 6, 8],
    'OtherColumn': [15, 25, 35, 45, 55]
}

# 创建两个 DataFrame
state = pd.DataFrame(data1)
statewindow = pd.DataFrame(data2)

# 逐行获取 'Max' 列的最大值
statewindow['Max'] = statewindow[['Max']].combine(state[['Max']], func=lambda s1, s2: s1.combine(s2, max))
statewindow['OtherColumn'] = statewindow[['Max']].combine(state[['Max']], func=lambda s1, s2: s1.combine(s2, min))
