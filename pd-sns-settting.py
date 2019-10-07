pd.set_opiton('display.max_columns',5)
pd.set_opiton('display.max_rows',4)

# seaborn
sns.set(rc={'figure.figsize':(20,20)})
# SAVEFIG
ax = sns.heatmap(df_corr, annot=True)
ax.get_figure().savefig("abc.png")
