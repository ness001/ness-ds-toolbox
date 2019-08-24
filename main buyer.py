import pandas as pd
bank = pd.read_csv('bank_additional_full.csv', sep=';')
# 提取购买者数据
buyer_filtered = bank[bank['y']=='yes'][['job', 'education']]
#main_buyer = buyer_filtered.apply(lambda x: x.value_counts().idxmax())
main_buyer=buyer_filtered.mode().iloc[0]
print(main_buyer)

(job admin.
education university.degree
Name: 0, dtype: object)




#######
import pandas as pd
bank = pd.read_csv('bank_additional_full.csv', sep=';')
#请在下方作答
result = bank.groupby(['job','education']).count().idxmax()[0]

print(result)
('admin.', 'university.degree')


# 查看出现频次较高的几种职业
fec.contbr_occupation.value_counts()[:10]

# 职业信息映射
occ_mapping = occ_mapping = {
'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
'INFORMATION REQUESTED':'NOT PROVIDED',
'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
'C.E.O.':'CEO'
}

# 如果没有映射关系的职业，则返回x
f1=lambda x: occ_mapping.get(x,x)
fec.contbr_occupation = fec.contbr_occupation.map(f1)

# 雇主信息映射
emp_mapping = {
'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
'INFORMATION REQUESTED':'NOT PROVIDED',
'SELF':'SELF-EMPLOYED',
'SELF EMPLOYED':'SELF-EMPLOYED'
}
f2=lambda x: emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f2)

# 查看频次出现前十职业
fec.contbr_occupation.value_counts()[:10]