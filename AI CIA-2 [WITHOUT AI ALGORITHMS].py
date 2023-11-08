#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num=int(input("How many 4-letter prompts will you enter : "))
a=[]
for i in range(num):
    string=input("Enter the prompt : ")
    a.append(string)
print(a)

f=[]
new=[]
for i in range(2,num-1):
    print("comparing : ", a[i-1],"and", a[i])
    print("we get : ")
    if a[i-1]==a[i]:
        print(a[i])
        f.append(a[i])
    elif a[i-1][1:4]==a[i][0:3]:
        print(a[i][0:3])
        f.append(a[i][0:3])
    elif a[i-1][2:4]==a[i][0:2]:
        print(a[i][0:2])
        f.append(a[i][0:2])
    elif a[i-1][3:4]==a[i][0:1]:
        print(a[i][0:1])
        f.append(a[i[0:1]])
    else:
        new.append(a[i-1])
        new.append(a[i])
    print("\n")

    
print(new)  
final=''.join(f)
print(a[0]+final+a[num-1])    


