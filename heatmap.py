# pairplot
from pandas.plotting import scatter_matrix
attributes=[ "x1", "x2","x3"]  # x of your interest
sns.pairplot(df[attributes])

#http://seaborn.pydata.org/generated/seaborn.heatmap.html
import seaborn as sns
sns.set(rc={'figure.figsize':(12,10)})
df_corr = df.corr()
ax = sns.heatmap(df_corr, annot=True,cmap="YlGnBu")
# 0.9.0 bug
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
# savefig
ax.get_figure().savefig("boston/X_corr_heatmap.png")