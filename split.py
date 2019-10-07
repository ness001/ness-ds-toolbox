# random split
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

for set_ in (train_set, test_set):
    set_.drop("income_cat", axis=1, inplace=True)


#stratified split
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing/x+y, housing["income_cat"]/y):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)