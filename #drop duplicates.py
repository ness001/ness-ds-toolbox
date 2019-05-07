#drop duplicates

import pandas as pd
raw_data = pd.read_csv('nba_rookie.csv')

# 打印出重复的样本，统计重复样本的个数
print (raw_data[raw_data.duplicated(keep=False)])
print (raw_data.duplicated(keep=False).value_counts())
# 去重
data_filtered = raw_data.drop_duplicates()

# 打印去重后，姓名相同的新秀
dup_name=data_filtered.duplicated(subset=['Name'])
print (data_filtered[dup_name].Name)

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


# 设置索引列
data_cleaned = data_filtered.set_index('Name')

#得到xx最大的人名，注意一定要有上一步设置索引
max_rookie = data_cleaned.idxmax()
PTS_max = max_rookie.loc['PTS']
REB_max = max_rookie.loc['REB']
TOV_max = max_rookie.loc['TOV']

print(PTS_max)
print(REB_max)
print(TOV_max)



import numpy as np

# 重置索引
data_cleaned.reset_index(inplace=True)

# 指定全局随机种子，使得每次运行代码得到相同的划分结果
np.random.seed(231)

# 指定测试集比例，并进行划分
test_ratio = 0.2
test = data_cleaned.sample(frac=0.2)
train = pd.concat([data_cleaned,test]).drop_duplicates(keep=False)#only on condition that there is no duplicated in cleaned data
#best way to get difference of two dfs must on condition of setting name as index
train = data_cleaned.drop(test.index)

#it means
0

df1.set_index('Name',inplace=True)
df2.set_index('Name',inplace=True)
newdf=df1.drop(df2.index)

#正负样本比例


import numpy as np

# 重置索引
data_cleaned.reset_index(inplace=True)

# 指定全局随机种子，使得每次运行代码得到相同的划分结果
np.random.seed(232)

# 指定测试集比例
test_ratio = 0.2

#
p=data_cleaned[data_cleaned['TARGET_5Yrs']==1]
n=data_cleaned[data_cleaned['TARGET_5Yrs']==0]
ptest=p.sample(frac=0.2)
ntest=n.sample(frac=0.2)
ind=ptest.index.append(ntest.index)

# 按照标签分层次划分训练测试集
test = data_cleaned.iloc[ind]
train = data_cleaned.drop(test.index)

# 验证正类负类比例
print("test_posi_ratio:", test[test['TARGET_5Yrs']==1].shape[0]/(test[test['TARGET_5Yrs']==1].shape[0]+train[train['TARGET_5Yrs']==1].shape[0]))
print("test_neg_ratio:", test[test['TARGET_5Yrs']==0].shape[0]/(test[test['TARGET_5Yrs']==0].shape[0]+train[train['TARGET_5Yrs']==0].shape[0]))




#replace multiple col name
import pandas as pd
loandata = pd.read_csv('loandata.csv')
loandata_transformed = loandata.copy()
loandata_transformed.columns = loandata.columns.map(lambda x: x.replace('_',' ').title())

print(loandata_transformed.columns)