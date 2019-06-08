#difference of df1 df2
#first we need to drop duplicates 
df1.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)
#then
diff_set=pd.concat[df1,df2].drop_duplicates(keep=False)