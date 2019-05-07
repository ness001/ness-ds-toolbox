#Let's train model!
*************************
modeling toolbox by ness001
*************************

df=df.drop(['B', 'C'], axis=1)#1代表列
X=df.loc[:,'a':'c']
y=df.loc[:,'d']#详情见data view toolbox

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0
	#1 signs train,2 signs test
x1, x2, y1, y2 = train_test_split(X, y, test_size = 0.25, random_state = 0)


xgboost.__version__

#xgboost
xgtrain = xgb.DMatrix(train.values, target.values)
xgtest = xgb.DMatrix(test.values)

params={
	'objective':'reg:squarederror',
	'eval_metric':'rmse'
}
#对于Python来说，如果要使用多个eval——metric，不能使用上述的字典mapping法,因为后面会替换前面的metric
#用list
eval_metric = ["auc","error"]
#自定义metric和objective
https://github.com/dmlc/xgboost/blob/master/demo/guide-python/custom_objective.py

def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    # return a pair metric_name, result. The metric name must not contain a colon (:) or a space
    # since preds are margin(before logistic transformation, cutoff at 0)
    return 'my-error', float(sum(labels != (preds > 0.0))) / len(labels)

# training with customized objective, we can also do step by step training
# simply look at xgboost.py's implementation of train
bst = xgb.train(param, dtrain, num_round, watchlist, obj=logregobj, feval=evalerror)



#训练伦次
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, dtrain, num_round)

preds = bst.predict(dtest)




reg:squarederror


