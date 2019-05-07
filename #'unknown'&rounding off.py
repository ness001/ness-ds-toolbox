#'unknown'&rounding off


#round off
#all
df.applymap(lambda x: '%.2f' % x)
#specific col
df['one'].map(lambda x: '%.2f' % x)

#convert unknown to NaN
def missing(x):
	if x=='unknown':
		return np.NaN
	return x
df.applymap(missing)