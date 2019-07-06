#!/usr/bin/env python
# coding: utf-8

# In[90]:


import os
import csv



# In[4]:



# In[42]:


pybankfile="budget_data.csv"


# In[291]:


#list to hold field names
pl_list=[]
#list to hold P&L values
plvalues = []
#list to hold date values
dates=[]
pldata={"dates","pl_list","delta"}


# In[300]:


with open("budget_data.csv","r") as pybankfile:
     csv_reader = csv.reader(pybankfile, delimiter=',') 
     row_count = sum(1 for row in csv_reader) 
     all_months = row_count-1
     print(all_months)


# In[204]:


with open("budget_data.csv", newline="") as pybankfile:
    csv_reader = csv.reader(pybankfile, delimiter=',')      
    columns = next(csv_reader)
    #print(f"CSV Header: {columns}"


# In[292]:


with open("budget_data.csv", newline="") as pybankfile:
    csv_reader = csv.DictReader(pybankfile) 
    for row in csv_reader:
        datevalue=str(row['Date'])
        dates.append(datevalue)
    print(dates)


# In[290]:


with open("budget_data.csv", newline="") as pybankfile:
    csv_reader = csv.DictReader(pybankfile) 
    total = 0
    for row in csv_reader:
        total += int(float(row['Profit/Losses']))
    print(total)


# In[252]:


pl_list = []
with open("budget_data.csv", newline="") as pybankfile:
    csv_reader = csv.DictReader(pybankfile) 
    for row in csv_reader:
        plvalue=row['Profit/Losses']
        pl_list.append(int(plvalue))
    print(pl_list)


# In[253]:


delta = []
for i in range(1,len(pl_list)):
    delta.append(pl_list[i]-pl_list[i-1])
print(delta)


# In[261]:


delta_total=0
for i in range(len(delta)):
    delta_total += delta[i]
print(delta_total)


# In[319]:


total = delta_total
total_items= (len(delta))
def mean(total,total_items):
    return total/total_items
avg_chg=mean(total,total_items)
print(avg_chg)


# In[324]:


max_increase=max(delta)
print(delta.index(max_increase))
print(dates[24])
print(max_increase)


# In[326]:


min_increase=min(delta)
print(delta.index(min_increase))
print(dates[43])
print(min_increase)


# In[312]:


print("Total months: %s" %all_months)


# In[336]:


f=open("output.txt","a")
print("Financial Summary \n----------------------------------",file==f) 
print("Total months: %s" %all_months,file==f) 
print("Total: %s" %total,file==f) 
print("Average Change: %s" %avg_chg,file==f) 
print("Greatest Increase: %s" %dates[24],max_increase,file==f) 
print("Greatest Decrease: %s" %dates[43],min_increase,file==f) 
f.close()


# In[335]:


print("Financial Summary \n----------------------------------") 
print("Total months: %s" %all_months) 
print("Total: %s" %total) 
print("Average Change: %s" %avg_chg) 
print("Greatest Increase: %s" %dates[24]) 
print("Greatest Decrease: %s" %dates[43])


# In[ ]:




