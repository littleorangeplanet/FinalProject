
# coding: utf-8

# In[4]:

import pandas as pd


# In[5]:

filepath = "/Users/weiweixu/Downloads/2016 Fall/Programming for Data Science/NYPD_Motor_Vehicle_Collisions.csv"

# change to your own path


# In[6]:

df = pd.read_csv(filepath)


# In[7]:

df


# In[8]:

import numpy as np


# In[9]:

df_1 = df.replace(['Unspecified'], np.nan)


# In[10]:

df_1


# In[11]:

# df_1[['ZIP CODE']] = df_1[['ZIP CODE']].fillna(int(0)).astype(int)


# In[12]:

df_1.index = np.arange(1, len(df_1) + 1)


# In[13]:

df_1


# In[14]:

#df.ix[1]


# In[15]:

#df_1.ix[[1]]


# In[16]:

#df_1.loc[[1]]


# In[17]:

#df_1.loc[1]


# In[18]:

#df_1.iloc[[1]]


# In[19]:

#df_1.iloc[1]


# In[20]:

#df_1.sort_values(['BOROUGH', 'ZIP CODE'])


# In[21]:

#gp_1 = df_1.groupby(['ZIP CODE'])


# In[22]:

#gp_zipcode = gp_1['ZIP CODE']


# In[23]:

#zipcode_count = gp_zipcode.agg(['count'])


# In[24]:

#type(zipcode_count)


# ### CREATE COLUMN 'YEAR' AND SORT BY IT.

# In[25]:

df_1['YEAR'] = [x[6:] for x in df_1['DATE']]


# In[34]:

year_count = df_1.groupby('YEAR').count().sort()


# In[35]:

print(year_count)


# ### CREATE COLUMN 'MONTH' AND SORT BY IT.

# In[36]:

df_1['MONTH'] = [x[:2] for x in df_1['DATE']]


# In[37]:

month_count = df_1.groupby('MONTH').count().sort()


# In[38]:

print(month_count)


# ### count by area (zip code and borough)

# In[26]:

zipcode_count = df_1.groupby(['ZIP CODE'])['ZIP CODE'].count()


# In[35]:

zipcode_count = zipcode_count.sort_values()


# In[27]:

type(zipcode_count)


# In[36]:

zipcode_count


# In[29]:

import matplotlib.pyplot as plt


# In[53]:

y = zipcode_count.values
x = zipcode_count.index
width = 24
pic_1 = plt.bar(x, y, width, color="orange")
plt.show()


# In[43]:

borough_count = df_1.groupby(['BOROUGH'])['BOROUGH'].count()


# In[44]:

borough_count


# In[50]:

y = borough_count.values
x = range(5)
labels = borough_count.index
width = 0.8
pic_2 = plt.bar(x, y, width, color="orange")
plt.xticks(x, labels)
plt.show()


# In[24]:

type(borough_count)


# In[25]:

borough_df = borough_count.to_frame("BoroughCount").reset_index()


# In[26]:

borough_df


# In[28]:

zipcode_df = zipcode_count.to_frame("ZipCount").reset_index()


# In[30]:

zipcode_df


# In[31]:

area = df_1[['BOROUGH', 'ZIP CODE']]


# In[32]:

area = area.dropna(how='all')


# In[33]:

area


# In[34]:

area = area.merge(borough_df, how='left',left_on='BOROUGH', right_on='BOROUGH')


# In[35]:

area = area.merge(zipcode_df, how='left',left_on='ZIP CODE', right_on='ZIP CODE')


# In[36]:

area


# In[38]:

area = area.sort_values(['BOROUGH', 'ZIP CODE']).reset_index()


# In[39]:

area

