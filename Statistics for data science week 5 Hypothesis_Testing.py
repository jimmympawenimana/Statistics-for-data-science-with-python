#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkST0151ENSkillsNetwork956-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Hypothesis Testing**
# 

# Estimated time needed: **30** minutes
# 

# The goal of hypothesis testing is to answer the question, “Given a sample and an apparent effect, what is the probability of seeing such an effect by chance?” The first step is to quantify the size of the apparent effect by choosing a test statistic (t-test, ANOVA, etc). The next step is to define a null hypothesis, which is a model of the system based on the assumption that the apparent effect is not real. Then compute the p-value, which is the probability of the null hypothesis being true, and finally interpret the result of the p-value, if the value is low, the effect is said to be statistically significant, which means that the null hypothesis may not be accurate.
# 

# ## Objectives
# 

# * Import Libraries
# * Lab exercises
#     * Stating the hypothesis
#     * Levene's Test for equality
#     * Preparing your data for hypothesis testing
# * Quiz
# 

# ----
# 

# ## Import Libraries
# 

# Import the libraries we need for the lab
# 

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats


# Read in the csv file from the URL using the request library
# 

# In[3]:


df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv')
df


# ## Lab Exercises
# 

# ### T-Test: Using the teachers' rating data set, does gender affect teaching evaluation rates?
# 

# We will be using the t-test for independent samples. For the independent t-test, the following assumptions must be met.
# * One independent, categorical variable with two levels or group
# * One dependent continuous variable
# * Independence of the observations. Each subject should belong to only one group. There is no relationship between the observations in each group.
# * The dependent variable must follow a normal distribution
# * Assumption of homogeneity of variance
# 

# State the hypothesis
# * $H_0: µ_1 = µ_2$ ("there is no difference in evaluation scores between male and females")
# * $H_1: µ_1 ≠ µ_2$ ("there is a difference in evaluation scores between male and females")
# 

# We can plot the dependent variable with a historgram
# 

# In[6]:


ax = sns.distplot(df['eval'],
                  bins=20,
                  kde=True,
                  color='turquoise',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
## we can assume it is normal


# We can use the Levene's Test in Python to check test significance
# 

# In[8]:


scipy.stats.levene(df[df['gender'] == 'female']['eval'],
                   df[df['gender'] == 'male']['eval'], center='mean')

# since the p-value is greater than 0.05 we can assume equality of variance


# Use the <code>ttest_ind</code> from the <code>scipy_stats</code> library
# 

# In[9]:


scipy.stats.ttest_ind(df[df['gender'] == 'female']['eval'],
                   df[df['gender'] == 'male']['eval'], equal_var = True)


# **Conclusion:** Since the p-value is less than alpha value 0.05, we reject the null hypothesis as there is enough proof that there is a statistical difference in teaching evaluations based on gender
# 

# ### ANOVA: Using the teachers' rating data set, does beauty  score for instructors  differ by age?
# 

# First, we group the data into cateries as the one-way ANOVA can't work with continuous variable - using the example from the video, we will create a new column for this newly assigned group our categories will be teachers that are:
# * 40 years and younger
# * between 40 and 57 years
# * 57 years and older
# 

# In[10]:


df.loc[(df['age'] <= 40), 'age_group'] = '40 years and younger'
df.loc[(df['age'] > 40)&(df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
df.loc[(df['age'] >= 57), 'age_group'] = '57 years and older'


# State the hypothesis
# * $H_0: µ_1 = µ_2 = µ_3$ (the three population means are equal)
# * $H_1:$ At least one of the means differ
# 

# Test for equality of variance
# 

# In[11]:


scipy.stats.levene(df[df['age_group'] == '40 years and younger']['beauty'],
                   df[df['age_group'] == 'between 40 and 57 years']['beauty'], 
                   df[df['age_group'] == '57 years and older']['beauty'], 
                   center='mean')
# since the p-value is less than 0.05, the variance are not equal, for the purposes of this exercise, we will move along


# First, separate the three samples (one for each job category) into a variable each.
# 

# In[12]:


forty_lower = df[df['age_group'] == '40 years and younger']['beauty']
forty_fiftyseven = df[df['age_group'] == 'between 40 and 57 years']['beauty']
fiftyseven_older = df[df['age_group'] == '57 years and older']['beauty']


# Now, run a one-way ANOVA.
# 

# In[13]:


f_statistic, p_value = scipy.stats.f_oneway(forty_lower, forty_fiftyseven, fiftyseven_older)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))


# **Conclusion:** Since the p-value is less than 0.05, we will reject the null hypothesis as there is significant evidence that at least one of the means differ.
# 

# ### ANOVA: Using the teachers' rating data set, does teaching  evaluation  score for instructors  differ  by age?
# 

# Test for equality of variance
# 

# In[14]:


scipy.stats.levene(df[df['age_group'] == '40 years and younger']['eval'],
                   df[df['age_group'] == 'between 40 and 57 years']['eval'], 
                   df[df['age_group'] == '57 years and older']['eval'], 
                   center='mean')


# In[15]:


forty_lower_eval = df[df['age_group'] == '40 years and younger']['eval']
forty_fiftyseven_eval = df[df['age_group'] == 'between 40 and 57 years']['eval']
fiftyseven_older_eval = df[df['age_group'] == '57 years and older']['eval']


# In[16]:


f_statistic, p_value = scipy.stats.f_oneway(forty_lower_eval, forty_fiftyseven_eval, fiftyseven_older_eval)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))


# **Conclusion:** Since the p-value is greater than 0.05, we will fail to reject the null hypothesis as there is no significant evidence that at least one of the means differ.
# 

# ### Chi-square: Using the teachers' rating data set, is there an association between tenure and gender?
# 

# State the hypothesis:
# * $H_0:$ The proportion of teachers who are tenured is independent of gender
# * $H_1:$ The proportion of teachers who are tenured is associated with gender
# 

# Create a Cross-tab table
# 

# In[17]:


cont_table  = pd.crosstab(df['tenure'], df['gender'])
cont_table


# Use the <code>scipy.stats</code> library and set correction equals False as that will be the same answer when done by hand, it returns: 𝜒2 value, p-value, degree of freedom, and expected values.
# 

# In[18]:


scipy.stats.chi2_contingency(cont_table, correction = True)


# **Conclusion:** Since the p-value is greater than 0.05, we fail to reject the null hypothesis. As there is no sufficient evidence that teachers are tenured as a result of gender.
# 

# ### Correlation: Using the teachers rating dataset, Is teaching  evaluation  score correlated with  beauty score?
# 

# State the hypothesis:
# * $H_0:$ Teaching evaluation score is not correlated with beauty score
# * $H_1:$ Teaching evaluation score is correlated with beauty score
# 

# Since they are both continuous variables we can use a pearson correlation test and draw a scatter plot
# 

# In[19]:


ax = sns.scatterplot(x="beauty", y="eval", data=df)


# In[20]:


scipy.stats.pearsonr(df['beauty'], df['eval'])


# **Conclusion:** Since the p-value  (Sig. (2-tailed)  < 0.05, we reject  the Null hypothesis and conclude that there  exists a relationship between  beauty and teaching evaluation score.
# 

# ## Practice Questions
# 

# ### Question 1: Using the teachers rating data set, does tenure affect teaching evaluation scores?
# * Use α = 0.05
# 

# In[22]:


## insert code here
scipy.stats.ttest_ind(df[df['tenure'] == 'yes']['eval'],
                   df[df['tenure'] == 'no']['eval'], equal_var = True)


# The p-value is less than 0.05 that means that - we will reject the null hypothesis as there evidence that being tenured affects teaching evaluation scores

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# scipy.stats.ttest_ind(ratings_df[ratings_df['tenure'] == 'yes']['eval'],
#                    ratings_df[ratings_df['tenure'] == 'no']['eval'], equal_var = True)
# The p-value is less than 0.05 that means that - we will reject the null hypothesis as there evidence that being tenured affects teaching evaluation scores
# -->
# 

# ### Question 2: Using the teachers rating data set, is there an association between age and tenure?
# * Discretize the age into three groups 40 years and youngers, between 40 and 57 years, 57 years and older (This has already been done for you above.)
# * What is your conclusion at α = 0.01 and α = 0.05?
# 

# In[24]:


## insert code here
cont_table  = pd.crosstab(df['tenure'], df['age_group'])
cont_table


# In[25]:


scipy.stats.chi2_contingency(cont_table, correction = True)


# At the α = 0.01, p-value is greater, we fail to reject null hypothesis as there is no evidence of an association between age and tenure
# At the α = 0.05, p-value is less, we reject null hypoothesis as there is evidence of an association between age and tenure

# Double-click **here** for a hint.
# 
# <!-- The hint is below:
# ## state your hypothesis
# Null Hypothesis: There is no association between age and tenure
# Alternative Hypothesis: There is an association between age and tenure
# 
# ## don't forget to create a cross tab of the data
# cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['age_group'])
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ## use the chi-square function
# scipy.stats.chi2_contingency(cont_table, correction = True)
# At the α = 0.01, p-value is greater, we fail to reject null hypothesis as there is no evidence of an association between age and tenure
# At the α = 0.05, p-value is less, we reject null hypoothesis as there is evidence of an association between age and tenure
# -->
# 

# ### Question 3: Test for equality of variance for beauty scores between tenured and non-tenured instructors
# * Use α = 0.05
# 

# In[26]:


## insert code here
scipy.stats.levene(df[df['tenure'] == 'yes']['beauty'],
                   df[df['tenure'] == 'no']['beauty'],                     
                   center='mean')


# Since the p-value is greater than 0.05, we will assume equality of variance of both groups

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ### use the levene function to find the p-value and conclusion
# scipy.stats.levene(ratings_df[ratings_df['tenure'] == 'yes']['beauty'],
#                    ratings_df[ratings_df['tenure'] == 'no']['beauty'], 
#                    center='mean')
# Since the p-value is greater than 0.05, we will assume equality of variance of both groups
# -->
# 

# ### Question 4: Using the teachers rating data set, is there an association between visible minorities and tenure?
# * Use α = 0.05
# 

# In[27]:


## insert code here
cont_table  = pd.crosstab(df['vismin'], df['tenure'])


# In[28]:


scipy.stats.chi2_contingency(cont_table, correction = True)


# Since the p-value is greater than 0.05, we fail to reject null hypothesis as there is no evidence of an association between visible minorities and tenure

# Double-click **here** for a hint.
# 
# <!-- The hint is below:
# ##State you hypothesis and Create a cross-tab:
# Null Hypothesis: There is no association between visible minorities and tenure
# Alternative Hypothesis: There is an association between visible minorities and tenure
# 
# cont_table  = pd.crosstab(ratings_df['vismin'], ratings_df['tenure'])
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ## run the chi2_contingency() on the contigency table
# scipy.stats.chi2_contingency(cont_table, correction = True)
# Since the p-value is greater than 0.05, we fail to reject null hypothesis as there is no evidence of an association between visible minorities and tenure
# -->
# 

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
