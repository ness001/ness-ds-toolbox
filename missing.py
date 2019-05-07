#pandas eda


df['a'].values_counts(dropna=False)

#show dtypes
df.dtypes
# change the dtype of a specific column
df['a']=df['a'].astype('float64') #int64 64=8byte*8bit=64 bit
#convert all objects to float and ignore strings
cols=df.columns[df.dtypes.eq('object')]
df[cols]=df[cols].apply(pd.to_numeric,error='ignore')
#convert specific col to specific dtype
type={'a':'float64','b':'int8'}#define a dictionary
df.astype(type)

#descriptive statistical analysis默认沿着index方向 axis=0
#calculate the mean of columns
df.mean(0) #axis=0 is index,means to calculate all indexes
#calculate the mean of obs, including all numeric values
df.mean(1)#axis=1 is columns,means to calculate on all column没有什么意义
#all kinds of stat calculate use 0/1 to differiente axix or index

#algebras
df.sub(df1,axis=1)#在一轴方向上进行操作，默认在1轴,	即在横（特征表头）上进行操作
df-df1
df.add(df1)
df.mul(df1)
df.div(df1)

#delete obs
df.dropna(axis=0,inplace=False)


#delete 
#drop,注意都是对观测进行处理而不是对列,即默认沿着index方向
#删除多列
def drp_multiple_col(col_names_list, df):
    df.drop(col_names_list, axis=1, inplace=True)
#drop obs
df.drop(['1','2'],axis=0)#default
#find duplicates and slice out non-dups
df.duplicated(keep=False)#return bool,False means keep all deplicates
df[~df.duplicated(keep='first')]
#drop duplicates
df.drop_duplicates(keep='first') #first is default,default axis=0
df.drop_duplicates('colname1')#only look into col1
#delete missing,axis=1 drop col,axis=0 default,drop obs
df.dropna(axis=0,how='any')#how='all',only delete those all nan
#计算删除obs个数
print(df.shape[0]-df_new.shape[0])




#missing values
#display nans
df.isnull().sum()#defalut axis=0
df.isnull().sum(1)#沿着列的方向求和，即统计出来obs的缺失数目
#检查缺失值
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)
#handle with missing，从后往前填充
data.fillna(0)
data.fillna(df2)
data.fillna(method='ffill',inplace=True)#用fore前值填充
data.fillna(method='bbill',inplace=True)#用后值填充
#对不同列使用不同填充，用dictionary
df.fillna({'col1':0,'col2':1})
df.fillna({'col1':df.col3-df.col2,'col2':df.col2.mean()})
#使用统计量进行填充
df.fillna(df.mean())
##拉格朗日多项式插值
from scipy.interpolate import lagrange
nonmissing=df[df.isnull()==False]
temp_index=list(nonmissing.index.values)
temp_value=list(nonmissing.values)
y_hat=lagrange(temp_index,temp_value)(3)
##线性插值
df.interpolate(method='values')#对index作为插值节点
##把缺失值归为其他类别
df.fillna('none')#python对象
df.fillna(np.nan)#方便变量间进行算术运算
-------------这个方法不好，可以直接用replace
df[df['a']=='missing'].fillna(np.nan)
------------------------
df['a']=df['a'].replace(Nan,'missing')


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
