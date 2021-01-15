#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
#Library to generate random list


# In[26]:


#Generate random 11 numbers from range 0-100
list1 = random.sample(range(0,100),11)


# In[27]:


#Sorted list 
list1.sort()
list1


# In[28]:


#Find out the start, mid and end points of the list
mid = int(len(list1)/2)
start= 0
end= len(list1)
print (mid,start,end)


# In[29]:



def closest_pair(p1,p2,list1):
    min_val= None
    for i in range (p1,p2):
        closest_val= abs(p1-p2)
        if not min_val:
            min_val=closest_val
        else:
            min_val=min(closest_val,min_val)

    return min_val
#Distance across the mid point
p = abs(list1[mid-1]-list1[mid+1])
#Closest distance on left side
p_left = closest_pair(0,mid,list1)
#Closest distance on right side
p_right = closest_pair(mid,end,list1)

#Random list generated 
print("The random list generate:",list1)
print("Mid point p= {0}\nMinimum left point p_left = {1}\nMinimum right point p_right ={2} ".format(p,p_left,p_right))

#Closest pair in the list
min_list= min(p,p_left,p_right)
print("Closest pair of the list {0}".format(min_list))


        


# In[ ]:





# In[ ]:




