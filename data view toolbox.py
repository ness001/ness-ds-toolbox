data 视图 view toolbox

**********************
* by ness002***********
***********************

cd data_path


#check for unique key
np.sort(np.unique(df['a']))
#check for num of unique key
df['a'].nunique()
#check for uniques key's frequency
df['a'].value_counts()


#change series types
#for example string to float32
df['a'].astype('float32')

#按照某列顺序进行排序
df.sort_values(by=['a','b'])

#slice几列，注意pandas中的slice和Python中不一样，它可以包含’d‘
df.loc[:,'a':'d']
#slice从a列到最后一列
df.loc[:,'a'::]
#slice 几行
df.iloc['apple':'cola',:]
#slice 几列几行 with step3
df.loc['w':'y', 'foo':'ant':3]


#选择分离的几列
df[['a','q','z','p']]

#看形状
print('df1:',frame_1.shape)
print('df2:',frame_2.shape)

#merge different df with same primary key  but different name
pd.merge(frame_1, frame_2, left_on='county_ID', right_on='countyid')
#left join
pd.merge(frame_1, frame_2, how='left', left_on='county_ID', right_on='countyid')
#right join
pd.merge(frame_1, frame_2, how='right', left_on='county_ID', right_on='countyid')



#change columns' name


