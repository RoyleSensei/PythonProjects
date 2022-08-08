#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[7]:


raw_csv_data = pd.read_csv("Absenteeism_data.csv")

raw_csv_data


# In[15]:


df = raw_csv_data.copy()


# In[14]:


df


# In[13]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None


# In[16]:


display(df)


# In[17]:


df.info()


# In[12]:


import pandas as pd

raw_csv_data = pd.read_csv("Absenteeism_data.csv")

type(raw_csv_data)


# In[24]:


df.drop(['ID'], axis = 1)


# In[19]:


df


# In[22]:


df = df.drop(['ID'], axis = 1)


# In[27]:


df


# In[29]:


df 


# In[ ]:





# In[30]:


1


# In[31]:


2


# In[33]:


3


# In[34]:


1+1


# In[35]:


4+5


# In[36]:


raw_csv_data


# # 'Reason for Absence' :

# In[38]:


df['Reason for Absence']


# In[39]:


df['Reason for Absence'].min()


# In[40]:


df['Reason for Absence'].max()


# In[41]:


pd.unique(df['Reason for Absence'])


# In[42]:


df['Reason for Absence'].unique()


# In[43]:


len(df['Reason for Absence'].unique())


# In[44]:


sorted(df['Reason for Absence'].unique())


# # get_dummies()

# In[10]:


import pandas as pd
raw_csv_data = pd.read_csv("Absenteeism_data.csv")
df = raw_csv_data.copy()

reason_columns = pd.get_dummies(df['Reason for Absence'])
reason_columns


# In[12]:


reason_columns = pd.get_dummies(df['Reason for Absence'])


# In[14]:


reason_columns['check'] = reason_columns.sum(axis =1)


# In[15]:


reason_columns


# In[16]:


reason_columns['check'].sum(axis=0)


# In[17]:


reason_columns['check'].unique()


# In[18]:


reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)


# In[19]:


reason_columns


# In[20]:


reason_columns['check'] = reason_columns.sum(axis =1)


# In[21]:


reason_columns


# # Group the Reasons for Absence:

# In[2]:


import pandas as pd

raw_csv_data = pd.read_csv("Absenteeism_data.csv")

df = raw_csv_data.copy()

df.columns.values


# In[3]:


reason_columns = pd.get_dummies(df['Reason for Absence'])
reason_columns

reason_columns.columns.values


# In[4]:


df = df.drop(['Reason for Absence'], axis = 1)


# In[5]:


df


# In[6]:


df = df.drop(['ID'], axis = 1)


# In[7]:


df


# In[8]:


reason_columns.loc[:, 15:17]


# In[9]:


reason_columns.loc[:, 1:14].max(axis = 1)


# In[10]:


reason_type_1 = reason_columns.loc[:,1:14].max(axis = 1)
reason_type_2 = reason_columns.loc[:,15:17].max(axis = 1)
reason_type_3 = reason_columns.loc[:,18:21].max(axis = 1)
reason_type_4 = reason_columns.loc[:,22:28].max(axis = 1)


# In[11]:


reason_type_1


# In[12]:


reason_type_2


# # Concatenate Column Values

# In[13]:


df


# In[14]:


df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis =1)
df


# In[15]:


df.columns.values


# In[16]:


column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours','Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']


# In[17]:


df.columns = column_names


# In[18]:


df.head()


# # Reorder Columns

# In[19]:


column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[20]:


df = df[column_names_reordered]


# In[21]:


df.head()


# # Create a Checkpoint

# In[22]:


df_reason_mod = df.copy()


# In[23]:


df_reason_mod


# # Date

# In[24]:


type(df_reason_mod["Date"][0])


# In[25]:


df_reason_mod["Date"] = pd.to_datetime(df_reason_mod["Date"], format = '%d/%m/%Y')


# In[26]:


df_reason_mod['Date']


# In[27]:


type(df_reason_mod['Date'][0])


# In[28]:


df_reason_mod.info()


# # Extract the Month Value

# In[29]:


df_reason_mod['Date'][0]


# In[30]:


df_reason_mod['Date'][0].month


# In[31]:


list_months = []
list_months


# In[32]:


for i in range(700):
    list_months.append(df_reason_mod['Date'][i].month)


# In[33]:


list_months


# In[34]:


len(list_months)


# In[35]:


df_reason_mod.shape


# In[36]:


df_reason_mod['Month Value'] = list_months


# In[37]:


df_reason_mod.head(20)


# # Extract the Day of the Week

# In[38]:


df_reason_mod['Date'][699].weekday()


# In[39]:


df_reason_mod['Date'][699]


# In[40]:


def date_to_weekday(date_value):
    return date_value.weekday()


# In[41]:


df_reason_mod['Day of the Week'] = df_reason_mod['Date'].apply(date_to_weekday)


# In[42]:


df_reason_mod['Day of the Week']


# In[43]:


df_reason_mod.head()


# In[44]:


df_reason_date_mod = df_reason_mod.copy()
df_reason_date_mod


# In[45]:


type(df_reason_date_mod['Transportation Expense'][0])


# In[47]:


type(df_reason_date_mod['Distance to Work'][0])


# In[48]:


type(df_reason_date_mod['Age'][0])


# In[49]:


type(df_reason_date_mod['Daily Work Load Average'][0])


# In[50]:


type(df_reason_date_mod['Body Mass Index'][0])


# # 'Education', 'Children', 'Pets'

# In[51]:


df_reason_date_mod['Education'].unique()


# In[54]:


df_reason_date_mod['Education'].value_counts()


# In[52]:


df_reason_date_mod['Children'].unique()


# In[55]:


df_reason_date_mod['Children'].value_counts()


# In[53]:


df_reason_date_mod['Pets'].unique()


# In[56]:


df_reason_date_mod['Pets'].value_counts()


# In[57]:


df_reason_date_mod['Education'] = df_reason_date_mod['Education'].map({1:0, 2:1, 3:1, 4:1})


# In[59]:


df_reason_date_mod['Education'].unique()


# In[60]:


df_reason_date_mod['Education'].value_counts()


# In[64]:


df_preprocessed=df_reason_date_mod
df_preprocessed.to_csv('Absenteeism_preprocessed.csv', index=False)


# In[ ]:





# In[ ]:




