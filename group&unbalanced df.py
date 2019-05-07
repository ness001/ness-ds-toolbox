df1['a'].groupby(df1['b'],df1['c']).unstack()


#custom cal
def mm(arr)
	return arr.max()-arr.min()


grouped=df['a'].groupby(df['b'])
grouped.agg(['mean','std',mm]) 