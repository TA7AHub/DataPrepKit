#!/usr/bin/env python
# coding: utf-8

# # Reading Data

# In[1]:


import pandas as pd
import numpy as np


# In[135]:


df= pd.read_excel("hand ball.xlsx")


# In[97]:


df


# # Data Summary

# In[99]:


summary_pandas = df.describe()


# In[100]:


Age = np.array(df['Age'])


# #  Handling Missing Values

# In[101]:


df.isna()


# In[32]:


df.isna().sum()


# In[82]:


df["Height"] =df["Height"].fillna(0)


# In[35]:


df["weight"] =df["weight"].fillna(0)


# # Category Data Encoding

# In[131]:


df = pd.get_dummies(df, columns=["Height"]) 


# In[138]:


df


# In[136]:


df = pd.get_dummies(df, columns=["weight"])


# In[137]:


df


# # Testing
# 

# In[46]:


summary_pandas


# In[47]:


Age


# In[105]:


df['statu'] = np.where(df['Age'] > 18,'refused','Accepted') 


# In[106]:


df


# In[120]:


def check_st(statu):
    if statu == 'refused':
        return 'Sorry, better luck next time'
    else:
        return 'Congrats, you are in our team'


# In[129]:


df = df['statu'].apply(check_st)


# In[130]:


df


# In[ ]:




