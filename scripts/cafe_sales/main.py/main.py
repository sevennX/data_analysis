#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

df = pd.read_csv("../../data_sets/cafe_sales/dirty_cafe_sales.csv")



# In[6]:


df.replace(["UNKNOWN","NaN","Null","ERROR"],np.nan,inplace=True)


# In[10]:


df["Quantity"] = df["Quantity"].astype("Int64")
df["Price Per Unit"] = df["Price Per Unit"].astype("Float64")
df["Total Spent"] = df["Total Spent"].astype("Float64")


# In[13]:


df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    format = "%Y-%m-%d",
    utc = False
)


# In[19]:


df["Total Spent"] = df["Total Spent"].fillna(df["Price Per Unit"] * df["Quantity"])


# In[ ]:


for item in df["Item"].dropna().unique():
    df["Payment Method"] = df["Payment Method"].fillna(df.groupby("Item").get_group(item)["Payment Method"].mode()[0])
    df["Location"] = df["Location"].fillna(df.groupby("Item").get_group(item)["Location"].mode()[0])



# In[39]:


df["Item"] = df["Item"].fillna(
    df.groupby("Price Per Unit")["Item"].transform("first")
)


# In[41]:


df["average_sales"] = df.groupby("Item")["Total Spent"].transform("mean")


# In[ ]:




