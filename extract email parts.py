import pandas as pd
import re 

# 匹配pattern
regex_pat = re.compile('([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})', flags=re.IGNORECASE)
#提取mail
print (mail_address.columns)
print (mail_address)
# 根据捕获组提取各个子字符串
mail_splited= mail_address['mail'].str.extract(regex_pat,expand=True)
print(mail_splited)
# 设置各列列名
mail_splited.columns = ['username','company','suffix']

# 与原“mail”列进行合并
mail_splited = mail_splited.join(mail_address)