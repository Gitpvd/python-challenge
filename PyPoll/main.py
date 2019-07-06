#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


pypollfile_path="election_data.csv"


# In[3]:


#pwd!


# In[4]:


with open("election_data.csv","r") as pypollfile:
     csv_reader = csv.reader(pypollfile, delimiter=',') 
     row_count = sum(1 for row in csv_reader) 
     all_votes = row_count-1
     print(all_votes)


# In[ ]:


ids=[]
county=[]
candidate=[]
election={"ids","county","candidate"}


# In[ ]:


candidate=[]
canvalue= str
with open("election_data.csv","r") as pypollfile:
    csv_reader = csv.DictReader(pypollfile,delimiter=',')
    for row in csv_reader:
        canvalue= row['Candidate']
        candidate.append(canvalue)


# In[ ]:


idvalue= int
with open("election_data.csv","r") as pypollfile:
    csv_reader = csv.DictReader(pypollfile,delimiter=',')
    for row in csv_reader:
        idvalue= row['Voter ID']
        ids.append(idvalue)


# In[ ]:


countyvalue= int
with open("election_data.csv","r") as pypollfile:
    csv_reader = csv.DictReader(pypollfile,delimiter=',')
    for row in csv_reader:
        countyvalue= row['County']
        county.append(countyvalue)


# In[ ]:


candidate_list=list(set(candidate))
print(candidate_list)


# In[ ]:


#Get total votes for each candidate
correy_votes=candidate.count("Correy")
otooley_votes=candidate.count("O'Tooley")
khan_votes=candidate.count("Khan")
li_votes=candidate.count("Li")

#Get % of total vote each candidate got
per_correy=((correy_votes/all_votes)*100)
per_otooley=((otooley_votes/all_votes)*100)
per_khan=((khan_votes/all_votes)*100)
per_li=((li_votes/all_votes)*100)

election_results={}
election_results.append[candidate_list]
print(election_results)

print(vote_per)
winner=max(vote_per)
election_results={
    candidate_list[0]:vote_per[0],
    candidate_list[1]:vote_per[1],
    candidate_list[2]:vote_per[2],
    candidate_list[3]:vote_per[3],
    }
print(election_results)
i=0,
for x,y in election_results.items():
    while i <= 3:
       if  winner == y:
                winner_name = x
    i += 1
print(winner_name)


# In[ ]:


f=open("output2.txt","a")
print("Election Results \n----------------------------------",file=f) 
print("Total votes: %s" %all_votes,file=f) 
print("----------------------------------",file=f)
print(candidate_list[0],":",per_correy,"%", "(", correy_votes,")",file=f)
print(candidate_list[1],":",per_otooley,"%", "(", otooley_votes,")",file=f)
print(candidate_list[2],":",per_khan,"%", "(", khan_votes,")",file=f)
print(candidate_list[3],":",per_li,"%", "(", li_votes,")",file=f)
print("----------------------------------",file=f)
print("Winner: %s", winner_name,file=f) 
f.close()


# In[ ]:


print("Election Results \n----------------------------------") 
print("Total votes: %s" %all_votes) 
print("----------------------------------")
print(candidate_list[0],":",per_correy,"%", "(", correy_votes,")")
print(candidate_list[1],":",per_otooley,"%", "(", otooley_votes,")")
print(candidate_list[2],":",per_khan,"%", "(", khan_votes,")")
print(candidate_list[3],":",per_li,"%", "(", li_votes,")")
print("----------------------------------")
print("Winner: %s", winner_name)


# In[ ]:




