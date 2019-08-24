import pandas as pd 
pd.Datafame(
    confusion_matrix(y_test,y_predict),
    columns=['predicted un-survived','predicted survived'],
    index=['actual un-survived','actual survived']
)