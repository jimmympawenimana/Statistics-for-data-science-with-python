#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot


# In[19]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv") 


# In[20]:


df


# ## Data Description
# 
# | Variable    | Description                                                                                                                                          |
# | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
# | minority    | Does the instructor belong to a minority (non-Caucasian) group?                                                                                      |
# | age         | The professor's age                                                                                                                                  |
# | gender      | Indicating whether the instructor was male or female.                                                                                                |
# | credits     | Is the course a single-credit elective?                                                                                                              |
# | beauty      | Rating of the instructor's physical appearance by a panel of six students averaged across the six panelists and standardized to have a mean of zero. |
# | eval        | Course overall teaching evaluation score, on a scale of 1 (very unsatisfactory) to 5 (excellent).                                                    |
# | division    | Is the course an upper or lower division course?                                                                                                     |
# | native      | Is the instructor a native English speaker?                                                                                                          |
# | tenure      | Is the instructor on a tenure track?                                                                                                                 |
# | students    | Number of students that participated in the evaluation.                                                                                              |
# | allstudents | Number of students enrolled in the course.                                                                                                           |
# | prof        | Indicating instructor identifier.                                                                                                                    |
# 

# ## Display information about the dataset
# 
# 1.  Structure of the dataframe
# 2.  Describe the dataset
# 3.  Number of rows and columns
# 

# In[23]:


df.head()


# In[27]:


df.info()


# In[28]:


df.shape


# Questions

# ### Can you identify whether the teachers' Rating data is a time series or cross-sectional?

# Print out the first ten rows of the data
# 
# 1.  Does it have a date or time variable? - No - it is not a time series dataset
# 2.  Does it observe more than one teacher being rated? - Yes - it is cross-sectional dataset
# 
# > The dataset is a Cross-sectional

# In[32]:


df.columns


# In[31]:


df.head(10)


# ### Find the mean, median, minimum, and maximum values for students

# Find Mean value for students

# In[36]:


df["students"].mean()


# In[37]:


df["students"].median()


# In[39]:


df["students"].min()


# In[40]:


df["students"].max()


# ### Create a histogram of the beauty variable and briefly comment on the distribution of data

# using the <code>matplotlib</code> library, create a histogram

# In[48]:


pyplot.hist(df['beauty'])


# ### Does average beauty score differ by gender? Produce the means and standard deviations for both male and female instructors.

# Use a group by gender to view the mean scores of the beauty we can say that beauty scores differ by gender as the mean beauty score for women is higher than men

# In[49]:


df.groupby('gender').agg({'beauty':['mean', 'std', 'var']}).reset_index()


# ### Calculate the percentage of males and females that are tenured professors. Will you say that tenure status differ by gender?

# First groupby to get the total sum

# In[50]:


tenure_count =df[df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()


# In[51]:


tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count


# ## Practice Questions

# ### Question 1: Calculate the percentage of visible minorities are tenure professors. Will you say that tenure status differed if teacher was a visible minority?

# In[56]:


tenure_count = df.groupby('minority').agg({'tenure': 'count'}).reset_index()
tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count


# ### Question 2: Does average age differ by tenure? Produce the means and standard deviations for both tenured and untenured professors.

# In[61]:


df.groupby('tenure').agg({'age':['mean', 'std']}).reset_index()


# ### Question 3: Create a histogram for the age variable.

# In[62]:


pyplot.hist(df['age'])


# ### Question 4: Create a bar plot for the gender variable.

# In[67]:


pyplot.bar(df.gender.unique(),df.gender.value_counts(),color=['pink','blue'])
pyplot.xlabel('Gender')
pyplot.ylabel('Count')
pyplot.title('Gender distribution bar plot')
pyplot.show()


# ### Question 5: What is the Median evaluation score for tenured Professors?

# In[71]:


df[df['tenure'] == 'yes']['eval'].median()

