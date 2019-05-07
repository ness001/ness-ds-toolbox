
cd data_path


import pandas as pd
df=pd.read_csv('abc.csv',index_col='a',parsed_dates=['date colums'],parse=parser,header=None,nrows=3)
#read excel
df=pd.read_excel('abc.xlsx',sheet_name=['first','second'])
df['first']#read the 'first' sheet
#rename cols
d={'one':'first','two':'second'}
df.rename(columns=d)
#查看行列个数
df.shape
df.shape[0]#obs
df.shape[1]#vars



#show data
df.head(3)
df.tail(3)
df.sample(3)

df.describe(include=['object'])
df.describe(include='all')
df.describe(percentiles=[0.05,0.7,0.9])

#select dtypes,return subset of df
df.select_dtypes(include=['number','datetime','timedelta'])
df.select_dtypes(exclude=['number'])
df.select_dtypes(include=['number'])#slice or numeric subsets


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


#选择分离的几列
df[['a','q','z','p']]


#merge different df with same primary key  but different name
pd.merge(frame_1, frame_2, left_on='county_ID', right_on='countyid')
#left join
pd.merge(frame_1, frame_2, how='left', left_on='county_ID', right_on='countyid')
#right join
pd.merge(frame_1, frame_2, how='right', left_on='county_ID', right_on='countyid')



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

#algebra of series
new_series=(pd['a']-pd['b']).astype('int64')
#slice of series


#panel to df
panel_data.to_frame()


#得到众数
main_buyer=buyer_filtered.mode().iloc[0]



