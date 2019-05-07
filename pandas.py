#read_csv
import pandas as pd
df=pd.read_csv('abc.csv',sep=';',encoding='gbk'
parse_dates=[u'中文'],index_col=u'中文索引列')
#custom variable name
df=pd.read_csv('abc.csv',header=None,names=['a','b','c'])
#custom index
df=pd.read_csv('abc.csv',index_col=0) #the first column



#slice df
df[:5] #display the first five rows

#encode question
import chardet
with open('abc.csv',mode='r') as f:
			s=f.readline().encode()
print(chardet.detect(s))

#read by fixed chunks
chunker=pd.read_csv("abc.csv",chunksize=4)#chunker is a iterator,TextFileReader
for piece in chunker:
	pass
#read by custom chunk size
df=pd.read_csv('abc.csv',iterator=True)#df is a iterator,TextFileReader
df.get_chunk(4)

#drop duplicates
df=df.drop_duplicates(keep='first') #retain the first occurrence


