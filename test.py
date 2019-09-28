import pandas as pd
from sklearn.model_selection import train_test_split
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
x=iris.drop(columns=['species'])
y=iris['species']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

def to_ndarray(df_list,key_list):
    '''pass a df list , return an ndarray-dictionary
    df_list=[x_train, x_test, y_train, y_test]
    key_list=['a','b','c','d']
    '''
    if len(df_list)!=len(key_list):
        print ('the length of df_list and key_list should be equal')
    length=len(df_list)
    ndarray_dict = {}
    for i in range(0,length):
        ndarray_dict[key_list[i]]=df_list[i].to_numpy()
        i=i+1
    return ndarray_dict

ndarray_dict=to_ndarray([x_train,x_test],['array1','array2'])