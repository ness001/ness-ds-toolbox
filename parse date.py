***注意对训练集和测试集都要做一样的操作****

#汇总
df=df.groupby(['A'])['c','d'].sum()#这时A会变成index
df.reset_index(replace=True)#把A从index里面释放出来了

#parse中文时间
import time
import datetime
time_str='2018年10月1日11时13分'
time_obj=time.strptime(time_str,'%Y年%m月%d日%H时%M分')
#convert to 英文格式
time.strptime('%Y-%m-%d-%H-%M')

#parse date when reading in files
import datetime
def parser(x):
    return datetime.datetime.strptime(x,"strptime org上面的格式")
df=pd.read_csv('abc.csv',parsed_dates=['date colums'],parse=parser)

#对时间统一格式化 
df['parsed_date']=pd.to_datetime(df[date],format="%m/%d/%y")
#如果少部分日期无法被解析
df['parsed_date']=pd.to_datetime(df[date],infer_datetime_format=True)
#如果还是没办法解析
df['parsed_date']=pd.to_datetime(df[date],error='coerce',format="%m/%d/%y")
#insert timestamp
def conver_str_datetime(df):
    df.insert(loc=2, column="timestamp", value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S")

#读取年月日时,星期几
df['year']=df['parsed_date'].dt.year
df['month']=df['parsed_date'].dt.month
df['day']=df['parsed_date'].dt.day
df['weekday']=df['parsed_date'].dt.dayofweek#从0开始排序的星期几，所以需要做处理
df['weekday']=df['parsed_date'].dt.dayofweek+1
df['hour']=df['parsed_date'].dt.hour

#对多列multiple columns进行label encoder编码
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df.apply(le.fit_transform)


#delete columns with missing  given proportion
for i in df:
    if sum(df[i].isna())>20300:
        del df[i]

#用函数做简单的encoder
def convert_cat2num(df):
    num_encode = { 'col_1': {'YES':1, 'NO':0},
                   'col_2': {'WON': 1, 'LOSE': 0, 'DRAW': 0}}
    df.replace(num_code, inplace=True)

#移除某列的字符串，按照正则表达式匹配
def remove_col_str(df):
    # remove a portion of string in a datafram column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)
    # remove all the characters after &#(including &#) for column-col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)

#移除空格，左边空格，右边空格，左右空格
def remove_col_white_space(df):
    # remove white space at the beginning of string
    df[col] = df[col].str.lstrip()

#用字符串条件合并两个列
def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True) #replace the 'pil' with empty space


#save to csv
pd.to_csv(index=False)#make sure the index is not saved
