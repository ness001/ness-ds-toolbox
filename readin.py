cd data_path

#READ_CSV
df=pd.READ_CSV('abc.csv',sep=';',encoding='gbk',parse_dates=['col1'],parse=parser/True,index_col='col0'/ 0 int,nrows=,usecols=,
	skiprows=,header=Noneifnoheader,names=whenNoneheader[],na_values=np.nan)#default index=none
#detect encoding
import chardet
with open('loan.csv',mode='r') as f:
	s=f.readline().encode()
print(chardet.detect(s))
#read by chunkers
chunker=pd.read_csv('abc.csv',chunksize=4)
for piece in chunker:
	pass
#READ WITH SPECIFIC SIZE of CHUNKER
df=pd.read_csv('abc.csv',iterator=True)
df.get_chunk(4)


#read excel
df=pd.read_excel('abc.xlsx',sheet_name=['first','second'])
df['first']#read the 'first' sheet

# read from dictionary
dict_ = {'key 1': 'value 1', 'key 2': 'value 2', 'key 3': 'value 3'}
pd.DataFrame([dict_])

#change index
df.reindex(columns=['age','sex','name'])
df.reindex(['r1','r2','r3'])
#set index
df.set_index('col1')
df.reset_index(inplace=True)
#修改列索引的名称,需要inplace=True
d={'three':'third','second':'two','one':'third'}
df.rename(columns=d,inplace=True)
df.rename(index=d)
df.rename(columns=str.upper)#把列名全部大写
df.rename(columns=str.lower)#把列名全部小写
df.rename(columns=lambda x:)#对列名做更加复杂的处理
loandata_transformed.columns = loandata.columns.map(lambda x: x.replace('_',' ').title())

#complicated 
columns_chi = '贷款数额|评级|评级细分|工作年限|是否拥有房屋|年收入|发贷日期|贷款状态|开户数量|还款总额|还贷利息总额' 
chinese=columns_chi.split('|')
eng=loan_data.columns
mapper={eng:chinese for eng,chinese in zip(eng,chinese)}
loan_chi=loan_data.rename(columns=mapper)

#multi indice
df.index.names=['ind1','ind2']
df.swaplevel(0,1,axis=1)
df.reorder_levels([2,1,0],axis=1)

#create series
pd.Series(data,index=index)
#create by index and value dicts
d={'a':0.1,'b'0.2,'c':0.3}
pd.Series(d)


#create dfs
pd.DataFrame(data,index,column)
#create by series
s=pd.Series([1,2,3],index=['a','b','c'])
pd.DataFrame(s,columns=['first'])
#CREATe by series and cols
data={'one':pd.Series([1,2,3],index=['a','b','c']),
'two':pdf.Series([2,3,4],index=['b','c','d'])}
pd.DataFrame(d)
#create by rows
data=[{'a':1,'b':2,'c':3},{'a':5,'b':10,'c':20}]
pd.DataFrame(data,index=[])



