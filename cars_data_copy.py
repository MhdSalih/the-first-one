#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np




# In[15]:


st.title('car details')
st.write('This is a table')

st.sidebar.file_uploader(label="upload your csv")



# In[16]:


st.write(df.head()
)


# In[17]:


st.write(df.tail())


# In[18]:


st.write(df.describe(
))


# In[19]:


st.write('This is a line_chart.')
st.line_chart(df)


# In[21]:


st.write('This is a area_chart.')
st.area_chart(df)
st.write('This is a bar_chart.')
st.bar_chart(df)


# In[ ]:




