#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd

# Import Data
top_1000 = pd.read_csv('top_1000_tiktokers.csv')
top_1000


# In[32]:


# Check Data
top_1000.info()
# Found1 have 2 null value in Name Column
# Found2 Unclean data type


# In[38]:


top_1000[top_1000['Name'].isnull()]

# Name could be null in tiktok, but the username must be unique in this app. 
# Therefore, we will use username to define these creator


# In[39]:


# Change dtype
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


# In[43]:


# Clean Data
top_1000['Subscribers Count'] = top_1000['Subscribers Count'].apply(value_to_float)
top_1000['Views. Avg'] = top_1000['Views. Avg'].apply(value_to_float)
top_1000['Likes. Avg'] = top_1000['Likes. Avg'].apply(value_to_float)
top_1000['Comments. Avg'] = top_1000['Comments. Avg'].apply(value_to_float)
top_1000['Shares. Avg'] = top_1000['Shares. Avg'].apply(value_to_float)


# In[44]:


top_1000


# In[47]:


top_1000.info()


# In[60]:


### Hypothesis 1:The company want to promoting the new products. The company is in the gaming industry. And the list below is all gaming content creator on tiktok
# I will choose the accounts with the most views because tiktok's algorithm is automatic content distribution.
# So those with a large stable number of views will be more suitable for promoting a new product to everyone.

top10_view = top_1000.sort_values('Views. Avg', ascending = False).head(10)
top10_view = top10_view[['Username','Tiktok Link','Views. Avg']]
top10_view


# In[64]:


### Hypothesis 2:The company want to promoting the new features
# I will choose the accounts with the most share because their view tend to share their video easier than others.
# If so, the content will be sent to more group and mess then both the company and its competitors's users will know about it 

top10_share = top_1000.sort_values('Shares. Avg', ascending = False).head(10)
top10_share = top10_share[['Username','Tiktok Link','Shares. Avg']]
top10_share


# In[68]:


### Hypothesis 2:The company has a media crisis and has provided an explanation, but still needs influencers to support and protect it.
# Those who have more like in their video will bring back the sympathize. We can seeding and filter in the comment sections to direct public options
top10_like = top_1000.sort_values('Likes. Avg', ascending = False).head(10)
top10_like = top10_like[['Username','Tiktok Link','Likes. Avg']]
top10_like


# In[ ]:





# In[ ]:





# In[ ]:





# In[59]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[30]:





# In[ ]:




