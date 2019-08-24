
#rename cols
d={'one':'first','two':'second'}
df.rename(columns=d)
#查看行列个数
df.shape
df.shape[0]#obs
df.shape[1]#vars

#seed
np.random.seed(42)

#show data
df.head(3)
df.tail(3)
df.sample(3)
df.sample(frac=0.3)

df.describe(include=['object'])
df.describe(include='all')
df.describe(percentiles=[0.05,0.7,0.9])


#maxindex
max=df.select_dtypes(include='number').idxmax()
max.loc['col1']
max.loc['col2']

#sort unique key
np.sort(np.unique(df['a']))
#check for num of unique key
df['a'].nunique() 
#freq of unique key
data['a'].value_counts(ascending=True)

#按照某列顺序进行排序
df.sort_values(by=['a','b'])

#slice几列，注意pandas中的slice和Python中不一样，它可以包含’d‘
df.loc[:,'a':'d']
#slice从a列到最后一列

df.loc[:,'a'::]
#slice 几行
df.loc['apple':'cola',:]
#slice 几列几行 with step3
df.loc['w':'y', 'foo':'ant':3]



#change columns' name

#set index with length,create dataframe
df=pd.DataFrame(range(len(bs)),columns=df.columns,data=df.values)

#create series,series is one-dim
pd.Series(data,index=index)
#ndarray to series
pd.Series(np.random.randn(4),index=['a','b','c','d'])#if no index it will be 012345
#dictionary to series key:value === index values
d={'a':1,'b':2,'c':3}
pd.Series(d)
#scalar to series
pd.Series(2,index=['a','b','c'])
#dataframe to seires
pd.Series(df['a'].values,index=df['b'].values)



#panel to df
panel_data.to_frame()


#得到众数
main_buyer=buyer_filtered.mode().iloc[0]



