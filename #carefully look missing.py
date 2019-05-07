#carefully look missing
import numpy as np
import pandas as pd
raw_data = pd.read_csv('nba_rookie.csv')
data_filtered = raw_data.drop_duplicates()

# 统计每个特征包含的缺失值数量
print (data_filtered.isnull().sum())
# percentage of missing
print (data_filtered.isnull().sum().sum()/len(data_filtered))
# 通过观察包含缺失值的样本，探索缺失值出现的原因
print (data_filtered[data_filtered.isnull()].head(3))
# 根据缺失值比例大小以及后续分析的目的来决定对缺失值做何处理，这里按照题目要求做删除处理
data_filtered = data_filtered.dropna()