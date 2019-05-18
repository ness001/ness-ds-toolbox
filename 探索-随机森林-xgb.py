import pandas as pd
df=pd.read_csv(r'C:\Users\ness\Documents\WeChat Files\ness001\FileStorage\File\2019-05\Merge.csv',index_col=0)
df.sample(3)
df.info()
df['TS股票代码'].nunique()
df['roe']=df['净利润 (元，下同)']/df['股东权益合计(含少数股东权益)']
df1=df[df['TS股票代码']=='002064.SZ']
df1.columns.tolist()#存货，固定资产，负债合计， '息税前利润','流动比率','速动比率'，'现金比率'
df1.shape
df1=df1.reset_index(drop=True)
import time
df1['报告期']=pd.to_datetime(df1['报告期'])
df1['季度']=df1['报告期'].dt.quarter
df1['年']=df1['报告期'].dt.year

#箱线图
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name())
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})
sns.boxplot(x='季度',y='营业收入',data=df1)
quarter4=df1[df1['季度']==4]

#核密度估计图
from scipy.stats import norm
sns.distplot(df1['营业收入'],fit=norm,kde=True)

#正态性检验
from scipy import stats
stats.normaltest(df1['营业收入'])#拒绝原假设

#折线图
sns.lineplot(x='年',y='营业收入',data=df1)
sns.lineplot(x='季度',y='营业收入',data=df1)

#对数差分，去异方差性和趋势
sns.lineplot(x='报告期',y='营业收入',data=df1)
df1['log']=np.log(df1['营业收入'])
sns.lineplot(x='报告期',y='log',data=df1)
df1['logdiff']=df1['log'].diff()
sns.lineplot(x='报告期',y='logdiff',data=df1)

#如何处理大量变量？变量相关性色图，变量与响应变量相关性色图
var_corr=df1.drop(['营业收入','营业总收入 (元，下同)','加:营业外收入','log','logdiff','报告期','年'],axis=1).corr()
# In[32]:
sns.set(rc={'figure.figsize':(20,20)})
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})
# In[33]:
sns.heatmap(var_corr,annot=False)#可见解释变量间信息重复较高
# In[34]:
sns.heatmap(df1.corr()[['营业收入']],annot=False)#从下图可以看出，营业收入和资产负债表诸多信息相关性较高

#简单的特征工程
labels=[-1,0,1]
df1['diff_rate']=(df1['营业收入'].diff())/df1['营业收入'].shift()
df1[['营业收入','diff_rate']].head(3)
cutted=pd.cut(df1['diff_rate'],3,labels=labels)
df1['diff_en']=cutted

#JMP聚类分析准备工作
df1.to_csv('F:\data\stock.csv',encoding='utf-8')
df2=df1.drop(['营业总收入 (元，下同)','加:营业外收入','log','报告期','diff_rate','TS股票代码'],axis=1)
df2.columns.tolist()

#主成分分解
#以之前的变量聚类结果作为指示，以0.02作为threshold，我们在这里选择13个主成分
from sklearn.decomposition import PCA
pca=PCA(n_components=13)
components=pca.fit_transform(df2.drop(['logdiff','营业收入','diff_en'],axis=1))
pdf=pd.DataFrame(data=components,columns=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13'])
pdf.head(3)
sns.heatmap(pdf.corr(),annot=False)


#一些特征工程
data=pd.concat([pdf,df2[['diff_en']]],axis=1)
data.fillna(0,inplace=True)
np.random.seed(100)
X=data.drop('diff_en',axis=1)
y=data['diff_en']
y_str=y.astype('str')
y_str[y_str=='-1']='bad'
y_str[y_str=='0']='normal'
y_str[y_str=='1']='good'

#随机森林
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(max_depth=5,n_estimators=10)
model.fit(X,y)
est=model.estimators_[1]
name=[i for i in X.columns]
y_str=y_str.values

#输出子树
from sklearn.tree import export_graphviz
export_graphviz(est,out_file='rf.dot',feature_names=name,class_names=y_str,rounded=True,proportion=True,
                precision=2,filled=True)
from subprocess import call
call([r'C:\Program Files (x86)\Graphviz2.38\bin\dot.exe','-Tpng','rf.dot','-o','rf.png','-Gdpi=600'])
from IPython.display import Image
Image(filename='rf.png')
preds=model.predict(X)

#CONFUSION MATRIX
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(preds,y)
from mlxtend.plotting import plot_confusion_matrix
fig,ax=plot_confusion_matrix(conf_mat=cm,figsize=(3,3))
perm=PermutationImportance(model,random_state=10).fit(X,y)

#RESUFFLE IMPORTANCE
import eli5
eli5.show_weights(perm,feature_names=X.columns.tolist())

#SHAP IMPORTANCE
import shap
from shap import initjs
initjs()
explainer=shap.TreeExplainer(model)
shap_values=explainer.shap_values(X,approximate=True)
shap.summary_plot(shap_values[1],X)
shap.summary_plot(shap_values[1],X,plot_type='bar')

#xgboost建模，TREE EXPLAINER
import xgboost
xgb=xgboost.train({'learning_rate':0.01},xgboost.DMatrix(X.values,label=y.values),100)
exp=shap.TreeExplainer(xgb)
vals=exp.shap_values(X.values)
shap.force_plot(explainer.expected_value[0],vals[0],X.iloc[0,:])
X.iloc[0,:]
y[0]
