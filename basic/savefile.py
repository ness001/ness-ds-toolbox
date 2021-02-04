text  = 'aaa'

# method 1
with open("./data/all_cate_pd_link.txt", "w") as text_file:
    print(text, file=text_file)
# method 2
your_data = {"Purchase Amount": 'TotalAmount'}
print(your_data,  file=open('D:\log.txt', 'w'))