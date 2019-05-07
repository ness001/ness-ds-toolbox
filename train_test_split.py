import numpy as np
import pandas as pd

# 读取待划分的数据集
admission = pd.read_csv('admissions.csv')

# 定义训练测试集划分函数
def train_test_split(data, y_name, test_ratio=0.3, random_state=266, stratify=False):    
    """用于将数据集随机划分成训练集和测试集
    
    参数
    ----
    data : dataframe, 原始数据集
    
    y_name : str, 标签名
    
    test_ratio : float, int, None, 测试集比例
    
    random_state : int, None, 随机种子
    
    stratify : boolean, 是否进行分层划分
    
    返回
    ----
    splitting : list, 包含划分结果的列表，依次为train_X, train_y, test_X, test_y
    
    """
    # 指定全局随机种子，使得每次运行代码得到相同的划分结果
    np.random.seed(random_state)
    
    if stratify:
        # 分层随机划分
        
        ## 分离各个类别样本，依次得到在测试集中的各类样本索引号，并添加到Index对象test_index中
        test_index = None
        for label in data[y_name].unique():
            data_single = data[data[y_name]==label]
            test_num = int(test_ratio * data_single.shape[0])          
            if test_index is not None:
                test_index = test_index.append(data_single.sample(test_num).index)
            else:
                test_index = data_single.sample(test_num).index
                
################## 请补全下面代码（作答部分） ######################

        ## 根据索引号划分训练测试集
        test = data.iloc[test_index]
        train = data.drop(test.index)
        
    else:
        # 普通随机划分
        
        test_num = None
        test = data.sample(frac=test_ratio)
        train = data.drop(test.index)
    
    # 拆分X和y
    train_X = train.drop(y_name,axis=1)
    train_y = train[y_name]
    test_X = test.drop(y_name,axis=1)
    test_y = test[y_name]
    splitting = [train_X,train_y,test_X,test_y]
    
    return splitting

# 利用函数对admission.csv进行训练测试集划分
train_X, train_y, test_X, test_y = train_test_split(admission, y_name='admit', test_ratio=0.25, random_state=266, stratify=True)



loan_merged = pd.merge(loan_info,account_info,left_index=True,right_on='user_id',how='inner').set_index('user_id')