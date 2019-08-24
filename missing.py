#every column
df.isnull().sum()
#degree of missing
df.isnull().sum().sum()/len(df)
#figure out the reason of missing value
df[df.isnull()].head(3)


df['a'].values_counts(dropna=False)

#delete obs
df.dropna(axis=0,inplace=False)

#find duplicates and slice out non-dups
df[~df.duplicated(keep='first')]


#delete missing,axis=1 drop col,axis=0 default,drop obs
df.dropna(axis=0,how='any')
#how='all' only delete those all nan
df.dropna(axis=0,how='all')

#计算删除obs个数
print(df.shape[0]-df_new.shape[0])




#missing values
#display nans
df.isnull().sum().sort_values(ascending=False)#defalut axis=0
df.isnull().sum(1)#沿着列的方向求和，即统计出来obs的缺失数目

#handle with missing，从后往前填充
data.fillna(0)
data.fillna(df2)
data.fillna(method='ffill',inplace=True)#用前值填充
data.fillna(method='bbill',inplace=True)#用后值填充
#对不同列使用不同填充，用dictionary
df.fillna({'col1':0,'col2':1})
df.fillna({'col1':anything,'col2':df.col2.mean()})
#使用统计量进行填充
df.fillna(df.mean())
#deal with 'unknown'
df.replace('unknown',np.nan)
#use df1 to fillna df2 or update df2	
df2.combine_first(df1)



##拉格朗日多项式插值
from scipy.interpolate import lagrange
nonmissing=df[df.isnull()==False]
temp_index=list(nonmissing.index.values)
temp_value=list(nonmissing.values)
y_hat=lagrange(temp_index,temp_value)(3)
##线性插值
df.interpolate(method='values')#对index作为插值节点


#基于模型的缺失值填补
nan_index=df[df['a'].isnull()].index.values
nonmissing_index=df[~df['a'].isnull()].index.values
trainX=df.iloc[nonmissing_index]
trainY=df.iloc[nonmissing_index,1]
testX=df.iloc[nan_index]
testY=df.iloc[nan_index,1]
#使用knn
#使用decision tree进行填补
from sklearn.tree import DecisionTreeRegressor

regr=DecisionTreeRegressor()
regr.fit(trainX,trainY)

testY_hat=regr.predict(testX)

df.iloc[nan_index]['missing_val']=testY_hat
