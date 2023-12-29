#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


Data = pd.read_csv("D:\Dataset\heart.csv")


# In[3]:


Data


# In[4]:


Data.head(3)


# In[5]:


Data.tail(3)


# In[6]:


Data.shape


# In[7]:


Data.info()


# In[8]:


Data.describe()


# In[9]:


Data.isnull()


# In[10]:


Data.isnull().sum()


# In[11]:


sns.heatmap(Data)


# In[12]:


data_dup= Data.duplicated().any()


# In[13]:


print(data_dup)


# In[14]:


data = Data.drop_duplicates()


# In[15]:


data


# In[16]:


data.shape


# In[17]:


Data


# In[18]:


Data.corr()


# In[64]:


plt.figure(figsize=(17,6))
sns.heatmap(Data.corr(),annot=True)
plt.show()


# In[20]:


Data.columns


# In[21]:


Data['target'].value_counts()


# In[22]:


Data['sex'].value_counts()


# In[23]:


sns.distplot(Data['age'],bins=20)
plt.show()


# In[24]:


Data.columns


# In[25]:


import seaborn as sns
sns.set_theme()


# In[63]:


sns.countplot(x="cp",hue="target",data=data)
plt.legend(labels=["No-disease","Disease"])
plt.title('CP with (No-disease, disease)')
plt.show()


# In[61]:


sns.countplot(x="target",data=data)
plt.xticks([1,0],['Male','Female'])
plt.title('Gender Distribution by Target')
plt.show()


# In[62]:


sns.countplot(x="sex",data=data)
plt.xticks([1,0],['Male','Female'])
plt.title('Gender Distribution by Count')
plt.show()


# In[59]:


plt.figure(figsize=(18,8))
sns.countplot(x="age", data=data)
plt.title('Age Distribution')
plt.show()


# In[32]:


# Visualize the distribution of the target variable
sns.countplot(x='target', data=data)
plt.title('Distribution of Heart Disease (1: Disease, 0: No Disease)')
plt.show()

# Correlation matrix heatmap
corr_matrix = Data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()


# In[34]:


# Example: Age distribution by target variable
plt.figure(figsize=(12, 8))
sns.histplot(Data[Data['target'] == 1]['age'], label='Heart Disease', kde=False)
sns.histplot(Data[Data['target'] == 0]['age'], label='No Heart Disease', kde=False)
plt.title('Age Distribution by Heart Disease')
plt.legend()
plt.show()


# In[44]:


# Box plot for cholesterol levels by heart disease
plt.figure(figsize=(12, 8))
sns.boxplot(x='target', y='chol', data=data)
plt.title('Cholesterol Levels by Heart Disease (0: No Disease, 1: Disease)')
plt.show()


# In[46]:


# Distribution of resting blood pressure by heart disease
plt.figure(figsize=(12, 8))
sns.histplot(data, x='trestbps', hue='target', multiple='stack', kde=True)
plt.title('Distribution of Resting Blood Pressure by Heart Disease')
plt.show()


# In[47]:


Data.columns


# In[57]:


# Bar plot for fasting blood sugar
plt.figure(figsize=(10, 6))
sns.barplot(x='fbs', y='target', data=data
        )
plt.title('Heart Disease by Fasting Blood Sugar (0: <120mg/dl, 1: >120mg/dl)')
plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Proportion of Heart Disease')
plt.show()


# In[ ]:




