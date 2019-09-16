#ordinal encoder
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
housing_cat_encoded[:10]
ordinal_encoder.categories_

#onthot encoder
from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
#alternatively
# cat_encoder = OneHotEncoder(sparse=False) #->dense
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_cat_1hot
housing_cat_1hot.toarray() #sparse -> dense
cat_encoder.categories_