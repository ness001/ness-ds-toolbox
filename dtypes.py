df_num=df.select_dtypes(include=['number'])
df_obj=df.select_dtypes(exclude=['number'])
df=df.select_dtypes(include=['number'],exclude=['datetime','timedelta'])
df=df.select_dtypes(include='all',exclude='object')

#to numpy ndarray
df_num.values
df_obj.values

#extract specific variable names
list(df_num)
list(df_obj)

d={'col1':'int64','col2':float}
df.astype(d)	