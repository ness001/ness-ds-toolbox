df_num=df.select_dtypes(include=['number'])
df_obj=df.select_dtypes(exclude=['number'])

#to numpy ndarray
df_num.values
df_obj.values

#extract specific variable names
list(df_num)
list(df_obj)