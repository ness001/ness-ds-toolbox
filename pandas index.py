#reset index
df=df.reset_index(drop=True)

#修改原来行索引的名称
df.index=['a','b','c']


#对行进行重排列，原来索引里没有的index的行会被设为nan
df.reindex(['a','b','c'])
#对列进行重排列，相当于可以更换两列
df.reindex(columns=['one','two','three'])
#用某一列作为索引值
df.set_index('col1')