#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkST0151ENSkillsNetwork956-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Visualization**
# 

# Estimated time needed: **30** minutes
# 

# In this lab, you will learn how to visualize and interpret data
# 

# ## Objectives
# 

# * Import Libraries
# * Lab Exercises
#     * Identifying duplicates
#     * Plotting Scatterplots
#     * Plotting Boxplots
# 

# ----
# 

# Import the libraries we need for the lab
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# Read in the csv file from the url using the request library
# 

# In[2]:


df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv')
df


# ## Lab Exercises
# 

# ###  Identify all duplicate cases using prof. Using all observations, find the average and standard deviation for age. Repeat the analysis by first filtering the data set to include one observation for each instructor with a total number of observations restricted to 94.
# 

# Identify all duplicate cases using prof variable - find the unique values of the prof variables
# 

# In[3]:


df.prof.unique()


# Print out the number of unique values in the prof variable
# 

# In[4]:


df.prof.nunique()


# Using all observations, Find the average and standard deviation for age
# 

# In[5]:


df['age'].mean()


# In[6]:


df['age'].std()


# Repeat the analysis by first filtering the data set to include one observation for each instructor with a total number of observations restricted to 94.
# > first we drop duplicates using prof as a subset and assign it a new dataframe name called no_duplicates_ratings_df
# 

# In[7]:


no_duplicates_df = df.drop_duplicates(subset =['prof'])
no_duplicates_df.head()


# > Use the new dataset to get the mean of age
# 

# In[8]:


no_duplicates_df['age'].mean()


# In[9]:


no_duplicates_df['age'].std()


# ### Using a bar chart, demonstrate if instructors teaching lower-division courses receive higher average teaching evaluations.
# 

# In[10]:


df.head()


# Find the average teaching evaluation in both groups of upper and lower-division
# 

# In[12]:


division_eval = df.groupby('division')[['eval']].mean().reset_index()
division_eval


# Plot the barplot using the seaborn library
# 

# In[13]:


sns.set(style="whitegrid")
ax = sns.barplot(x="division", y="eval", data=division_eval)


# ### Plot the relationship between age and teaching evaluation scores.
# 

# Create a scatterplot with the scatterplot function in the seaborn library
# 

# In[14]:


ax = sns.scatterplot(x='age', y='eval', data=df)


# ### Using gender-differentiated scatter plots, plot the relationship between age and teaching evaluation scores.
# 

# Create a scatterplot with the scatterplot function in the seaborn library this time add the <code>hue</code> argument
# 

# In[15]:


ax = sns.scatterplot(x='age', y='eval', hue='gender',
                     data=df)


# ### Create a box plot for beauty scores differentiated by credits.
# 

# We use the <code>boxplot()</code> function from the seaborn library
# 

# In[17]:


ax = sns.boxplot(x='credits', y='beauty', data=df)


# ### What is the number of courses taught by gender?
# 

# We use the <code>catplot()</code> function from the seaborn library
# 

# In[18]:


sns.catplot(x='gender', kind='count', data=df)


# ### Create a group histogram of taught by gender and tenure
# 

# We will add the <code>hue = Tenure</code> argument
# 

# In[19]:


sns.catplot(x='gender', hue = 'tenure', kind='count', data=df)


# ### Add division as another factor to the above histogram
# 

# We add another argument named <code>row</code> and use the division variable as the row
# 

# In[20]:


sns.catplot(x='gender', hue = 'tenure', row = 'division',
            kind='count', data=df,
            height = 3, aspect = 2)


# ### Create a scatterplot of age and evaluation scores, differentiated by gender and tenure
# 

# Use the <code>relplot()</code> function for complex scatter plots
# 

# In[21]:


sns.relplot(x="age", y="eval", hue="gender",
            row="tenure",
            data=df, height = 3, aspect = 2)


# ### Create a distribution plot of teaching evaluation scores
# 

# We use the <code>distplot()</code> function from the seaborn library, set <code>kde = false</code> because we don'e need the curve
# 

# In[22]:


ax = sns.distplot(df['eval'], kde = False)


# ### Create a distribution plot of teaching evaluation score with gender as a factor
# 

# In[23]:


## use the distplot function from the seaborn library
sns.distplot(df[df['gender'] == 'female']['eval'], color='green', kde=False) 
sns.distplot(df[df['gender'] == 'male']['eval'], color="orange", kde=False) 
plt.show()


# ### Create a box plot - age of the instructor by gender
# 

# In[24]:


ax = sns.boxplot(x="gender", y="age", data=df)


# ### Compare age along with tenure and gender
# 

# In[25]:


ax = sns.boxplot(x="tenure", y="age", hue="gender",
                 data=df)


# ## Practice Questions
# 

# ### Question 1: Create a distribution plot of beauty scores with Native English speaker as a factor
# * Make the color of the native English speakers plot - orange and non - native English speakers - blue
# 

# In[28]:


## insert code
## use the distplot function from the seaborn library
sns.distplot(df[df['native'] == 'yes']['beauty'], color='orange', kde=False) 
sns.distplot(df[df['native'] == 'no']['beauty'], color="blue", kde=False) 
plt.show()


# ### Question 2: Create a Horizontal box plot of the age of the instructors by visible minority
# 

# In[32]:


## insert code
ax = sns.boxplot(x="age", y="minority", data=df)


# ### Question 3: Create a group histogram of tenure by minority and add the gender factor
# 

# In[33]:


## insert code
sns.catplot(x='tenure', hue = 'minority', row = 'gender',
            kind='count', data=df,
            height = 3, aspect = 2)


# ### Question 4: Create a boxplot of the age variable
# 

# In[34]:


## insert code
ax = sns.boxplot(y='age', data=df)


# ## Authors
# 

# [Aije Egwaikhide](https://www.linkedin.com/in/aije-egwaikhide/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkST0151ENSkillsNetwork956-2022-01-01) is a Data Scientist at IBM who holds a degree in Economics and Statistics from the University of Manitoba and a Post-grad in Business Analytics from St. Lawrence College, Kingston. She is a current employee of IBM where she started as a Junior Data Scientist at the Global Business Services (GBS) in 2018. Her main role was making meaning out of data for their Oil and Gas clients through basic statistics and advanced Machine Learning algorithms. The highlight of her time in GBS was creating a customized end-to-end Machine learning and Statistics solution on optimizing operations in the Oil and Gas wells. She moved to the Cognitive Systems Group as a Senior Data Scientist where she will be providing the team with actionable insights using Data Science techniques and further improve processes through building machine learning solutions. She recently joined the IBM Developer Skills Network group where she brings her real-world experience to the courses she creates.
# 

# ## Change Log
# 

# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# | 2020-08-14  | 0.1  | Aije Egwaikhide  |  Created the initial version of the lab |
# 

#  Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkST0151ENSkillsNetwork956-2022-01-01).
# 
