#calculate默认沿着index轴 axis=0计算
df['col1'].mean()
df['col1'].std()
df.sum()

#表示需要匹配的轴,	defaul:axis=1
df_mean=df.mean()
df.sub(df_mean,axis=1)
(df-df_mean)/df_std

df.cov()
df.corr()


#重排列
df=df.sample(len(df))
#is equal to
df=df.take(np.random.permuation(len(df)))

#离散化，映射
mapper={'good':1,'med':0,'bad':-1}
df['a'].replace(mapper,inplace=true)


#merge with var
pd.merge(df1,df2,left_on='v1',right_on='v2',how='outer')
#merge with index
pd.merge(df1,df2,left_on='v1',right_index=True)


#index concat
pd.concat([df1,df2],on=['col1','col2'])
#col concat
pd.concat([df1,df2],axis=1,join='inner',ignore_index=True)
pd.concat([df1,df2],axis=1,keys=['first','second'])
pd.concat([df1,df2],axis=1,join_axes=[df1.index])

#first/last/false 意味着保留第一个重复值，最后一个重复值和所有重复值
#merge different df with same primary key  but different name
pd.merge(left,right,on='key',how='outer/left/right/inner',indicator=True/'ind_col1')
pd.merge(frame_1, frame_2, left_on='county_ID', right_on='countyid')
#left join
pd.merge(frame_1, frame_2, how='left', left_on='county_ID', right_on='countyid',suffixes=('_left','_right'))
pd.merge(df1,df2,left_index=True,right_on='key2')



#return boolean series
print(df[df.duplicated(keep=first)])
print(df[df.duplicated(subset='col1')])
print(df.duplicated().value_counts())
#drop rows
df.drop_duplicates('col1')
df.drop_duplicates()
#first : Drop duplicates except for the first occurrence.<- default
#last : Drop duplicates except for the last occurrence.
#False : Drop all duplicates.Ω
df.drop_duplicates(keep='first') 

#del a column
df=df.drop(columns=['col2','col100'])
df=df.drop(index=['row1','row2'])
df.drop(needtobedel.index)
del df['col1']
y=df.pop('col1')

#convert to discrete variable
from sklearn.cluster import KMeans
slice=df[‘a’]
values=slice.values#get√ ndarray

model=Kmeans(n_cluster=4,n_jobs=4)
model.fit(values.reshape(len(slice),1))

sorted_centers=pd.DataFrame(data=model.cluster_centers_).sort_values(axis=0,ascending=True)#相邻两个中心点的均值
edegs=sorted_centers.rolling(2,center=False).mean()[1:]#因为第0行是nan，所以从1开始
bins=[slice[0],slice[len(slice)-1]]
bins[1:1]=edges[0].values.tolist()
cutted=pd.cut(slice, bins,include_lowest=True)#包含端点

#标准化，即中心化，所有方法必须考虑原来数据的分布可能是什么
#检验是否正态,h0是正态
stats.normaltest(df['a'].values)
#z-score ,即减去均值除以方差，大样本下有渐近正态性，必须考虑原来数据分布是什么样的，不然标准化后改变很多分布的信息
from sklearn import preprocessing
df['a']=preprocessing.scale(df['a'])
###
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
df = sc.fit_transform(df['a'].values.reshape(-1,1))
sc.mean_
sc.var_
#对异常值很敏感，因为把最大最小值作为分母来消除量纲
#另外如果获得了新数据，超过原来最大最小值，那么所有数据都要重新进行标准化
from sklearn.preprocessing import MinMaxScaler
s = MinMaxScaler(feature_range(0,1))
s.fit_transform(df['a'].values.reshape(-1,1))
#logistics标准化，让很大的数值很小的数值放在-1到1区间内
####
#box-cox变换,让本来不是正态数据变化为渐近正态，不过那样不就改变了原来数据的分布吗？？？
from scipy import stats
normalized_data = stats.boxcox(original_data)


#二值转化
from sklearn.preprocessing import Binarzier
b=Binarzier(threshold=10)
df['col1_bi']=b.fit_transform(df[['col_bi']])
#onehot编码，结果变为多列
encode=pd.get_dummies(data['a'],prefix='col1_')

#字符串操作
#提取邮箱
regex_pat = re.compile('([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})', flags=re.IGNORECASE)







