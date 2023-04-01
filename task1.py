#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1},{1:34, "key2": [55, 67, 78, 89], 4: (45,22, 61, 34)}, [56, 'data science'], 'Machine Learning']# phase 1
def flatlist(list1):
    flist=[]
    for i in list1:
        if type(i)==list or type(i)==tuple or type(i)==set:
            for element in i:
                flist.append(element)
        elif type(i)==dict:
            temp_list=list(i.items())
            for i in temp_list: # [(1, 34), ('key2', [55, 67, 78, 89]), (4, (45, 22, 61, 34))
                for element in i:
                    if type(element)==list or type(element)==tuple:
                        for j in element:
                            flist.append(j)
                    else:
                        flist.append(element)
        else:
            flist.append(i)
    return flist
list2=flatlist(list1)
print(list2)
a=1
for i in list2:
    if type(i)==int:
        a=a*i
print(a)


# In[ ]:




