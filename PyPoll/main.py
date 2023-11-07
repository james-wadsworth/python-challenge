#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


# Initialize a variable to hold the data file path
csvpath = "Resources/election_data.csv"
csvpath


# In[3]:


# Create a dataframe from the csv file data, then check that it was created properly
df = pd.read_csv(csvpath)
df.head()


# In[4]:


# Count the total number of votes by counting the total of the candidate row
total_votes = df["Candidate"].count()
total_votes


# In[10]:


# Find a complete list of candidates who received votes, the total percentage and number of votes received by each
# first print out the list of candidates and their vote totals. Convert that table to a dataframe
vote_totals = df["Candidate"].value_counts()
votes_df = pd.DataFrame(vote_totals)
votes_df


# In[12]:


# Working within this dataframe, add a column that calculates the percentage of votes received by each candidate
votes_df["Percentage of Vote"] = votes_df["Candidate"]/votes_df["Candidate"].sum() * 100
votes_df


# In[13]:


# Export this to a text file
# Set the file path
file_path = "votes_analysis.txt"
votes_df.to_csv(file_path)

