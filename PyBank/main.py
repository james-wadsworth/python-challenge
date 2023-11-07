#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import Pandas
import pandas as pd
import locale


# In[2]:


# Initialize a variable to hold the file path to the PyBank csv file
csvpath = "Resources/budget_data.csv"
csvpath


# In[17]:


# Create a pandas dataframe from the csv data
budget_file_df = pd.read_csv(csvpath, encoding="UTF-8")

#Check that the dataframe was properly created
budget_file_df.head(5)


# In[32]:


# Count the total number of months for which there is data in the file
total_months = budget_file_df["Date"].count()
total_months


# In[5]:


# Calculate the total net profit in the Profit/Losses column for the entire period
net_profit = budget_file_df["Profit/Losses"].sum()
net_profit


# In[19]:


# Find the average month-over-month change in Profit / Losses
# First, create a new column in the dataframe that shifts Profit/Losses up by one month to allow for ease of calculation
budget_file_df["Next Month"] = budget_file_df["Profit/Losses"].shift(-1)
budget_file_df.head()


# In[20]:


# Create another column that calculates the month-over-month change in Profit/Losses holds the change
budget_file_df["Delta"] = budget_file_df["Next Month"] - budget_file_df["Profit/Losses"]
budget_file_df.head()


# In[23]:


# Find the average change, or "Delta"
average = budget_file_df["Delta"].mean()
average


# In[24]:


# Find the greatest increase between months in "Profit/Losses"
increase = budget_file_df["Delta"].max()
increase


# In[25]:


# Find the greatest decrease between months in "Profit/Losses"
decrease = budget_file_df["Delta"].min()
decrease


# In[34]:


# Create a new summary dataframe that holds and displays the summary information about the PyBank budget file
Summary_df = pd.DataFrame({"Summary":
              ["Total Months", "Total Net Profit", 
               "Average Monthly Change", 
               "Greatest MoM Increase in Profits", 
               "Greatest MoM Decrease in Profits"], 
              "Amount": 
              [total_months,
               net_profit, average, 
               increase, 
              decrease]})

# Set the index
Summary_df.set_index("Summary", inplace=True)

# Set the locale to US to be able to format data as USD
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# Apply the local to the Amount column to format it as USD
Summary_df["Amount"] = Summary_df.apply(lambda row: 
                                        locale.currency(row["Amount"], grouping=True) 
                 if row.name != 1 else row["Amount"], axis=1)

Summary_df


# In[35]:


# Export this table as a text file

# First set the file path
file_path = "summary.csv"

# Export the summary dataframe to this file
Summary_df.to_csv(file_path), index=False, encoding="en_US.UTF-8")

