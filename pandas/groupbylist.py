df.groupby('a')['b'].apply(set)
df.groupby('a')['b'].groups.keys()
