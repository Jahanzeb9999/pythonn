#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[6]:


Pybank = os.path.join("budget_data.csv")


# In[7]:


profit = []
monthly_changes = []
date = []


# In[9]:


count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0


with open(Pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1 

        date.append(row[0])

        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        average_change_profits = (total_change_profits/count)
      
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]


# In[11]:


print(total_profit)


# In[ ]:




