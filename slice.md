# split out rows with row integer label
```
your df
	max_speed	shield
7	1	2
8	4	5
9	7	8

```

```
>>> df.loc[7:9]
   max_speed  shield
7          1       2
8          4       5
9          7       8
```

# split out rows with row index
```
df[0:3]
```