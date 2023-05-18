list=['3','5','3','2','1','5']
list_uniq=[]
for item in list:
    if item not in list_uniq:
        list_uniq.append(item)
print(list_uniq)