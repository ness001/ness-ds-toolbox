import pandas as pd 
data = pd.read_csv('user_review.csv')

# 请在下方作答 #
print data['User continent'].value_counts(dropna=False)
encode_uc=pd.get_dummies(data['User continent'],prefix='User continent_')
encode_uc.head()

