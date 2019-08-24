

dfgb=df.groupby('col1')
dfgb.size()
dfgb.mean()

#multi index
dfgb=df.groupby(['col1','col2'])

#get group method
dfgb.get_group('kind1')
#use dict method
splitted = dict(list(bank.groupby('y')))
splitted['kind1']

#get grouped values
dfgb[['col3']]

#use mapper
df.groupby(mapper func)

#cal on group as unsual
dfgb.agg()

#custom cal
def mm(arr)
	return arr.max()-arr.min()
grouped.agg(['mean','std',mm]) 