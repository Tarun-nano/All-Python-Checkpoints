#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


train=pd.read_csv("C:\\Users\91969\Desktop\\housetrain.csv")
test=pd.read_csv("C:\\Users\91969\Desktop\\housetest.csv")


# In[9]:


train.head()


# In[11]:


train.shape


# In[10]:


new_train=train.drop("Id",axis=1)
new_test=test.drop("Id",axis=1)


# In[15]:


dummytrain=pd.get_dummies(new_train)
dummytest=pd.get_dummies(new_test)


# # Check the linearity

# h0: Data is linear
# 
# h1:data is not linear
#     

# In[32]:


import statsmodels.api as sms


# In[33]:


y=dummytrain.SalePrice
x=dummytrain.drop(columns="SalePrice")
X=dummytest


# In[34]:


model=sms.OLS(y,x).fit()


# In[35]:


model.summary()


# In[36]:


sms.stats.diagnostic.linear_rainbow(model)


# In[43]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=1,test_size=.20)
lr.fit(pd.DataFrame(train_x),train_y)


# In[ ]:





# In[ ]:




