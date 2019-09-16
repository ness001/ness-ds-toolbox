corr_matrix_df = df.corr()
corr_matrix_df["target"].sort_values(ascending=False)

# f4*4 plot
from pandas.plotting import scatter_matrix

attributes = ["y", "x1", "x2",
              "x3"]# x of your interest
scatter_matrix(df[attributes], figsize=(12, 8))
save_fig("scatter_matrix_plot")

# cm plot