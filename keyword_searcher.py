import pandas as pd
import re
import math
import matplotlib.pyplot as plt 


"""
    This is the list of keywords, and each keyword should represents a question/sub-question. Cannot use multiple keywords for the same queston.
    To use the codes, ONLY change keywords here. 
    |
    |
    |
   \ /
"""
keywords = ['working credit', 'working families', 'greater boston legal services', 'lawyers clearing hous', 'prophetic resistance', 'CORI', 'case'] 


#NO NEED TO CHANGE CODES BELOW

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""new registration"""


file_new = 'New_registration.csv'
df_new = pd.read_csv(file_new)

# Filter out rows where 'Services Requested and Offered' is blank
df_new = df_new[df_new['Services_Requested_and_Offered'].notna()]

# Initialize a dictionary to count appearances
keyword_counts_new = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_new = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_new.iterrows():
    text = row['Services_Requested_and_Offered']
    total_cases_new += 1  # Increment total cases for each non-blank row
    for keyword in keywords:
        appearances = count_keyword_appearances(text, keyword)
        if appearances > 0:
            keyword_counts_new[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Robert"""


file_Robert = 'Robert.csv'
df_Robert = pd.read_csv(file_Robert) 

# Initialize a dictionary to count appearances
keyword_counts_Rob = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Rob = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Robert.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Rob += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Rob[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Dominique"""


file_Dom = 'Dominique.csv'
df_Dom = pd.read_csv(file_Dom)

# Initialize a dictionary to count appearances
keyword_counts_Dom = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Dom = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Dom.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Dom += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Dom[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Divad"""


file_Divad = 'Divad.csv'
df_Divad = pd.read_csv(file_Divad)

# Initialize a dictionary to count appearances
keyword_counts_Divad = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Divad = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Divad.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Divad += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Divad[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Rachelle"""


file_Rachelle = 'Rachelle.csv'
df_Rachelle = pd.read_csv(file_Rachelle)

# Initialize a dictionary to count appearances
keyword_counts_Rachelle = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Rachelle = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Rachelle.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Rachelle += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Rachelle[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Khalid"""


file_Khalid = 'Khalid.csv'
df_Khalid = pd.read_csv(file_Khalid) 

# Initialize a dictionary to count appearances
keyword_counts_Khalid = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Khalid = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Khalid.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Khalid += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Khalid[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""SandyHousing"""


file_Sandy = 'SandyHousing.csv'
df_Sandy = pd.read_csv(file_Sandy)

# Initialize a dictionary to count appearances
keyword_counts_Sandy = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_Sandy = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_Sandy.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_Sandy += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_Sandy[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Incarcerated_waitlist"""


file_incarcerated = 'Incarcerated_waitlist.csv'
df_incarcerated = pd.read_csv(file_incarcerated)

# Initialize a dictionary to count appearances
keyword_counts_incarcerated = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_incarcerated = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_incarcerated.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_incarcerated += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_incarcerated[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Inactive"""


file_inactive = 'Inactive.csv'
df_inactive = pd.read_csv(file_inactive)

# Initialize a dictionary to count appearances
keyword_counts_inactive = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_inactive = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_inactive.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_inactive += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_inactive[keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Low_risk"""


file_lowrisk = 'Low_risk.csv'
df_lowrisk = pd.read_csv(file_lowrisk) 

# Initialize a dictionary to count appearances
keyword_counts_low = {keyword: 0 for keyword in keywords}

# Initialize counter for total number of cases
total_cases_low = 0

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Iterate through each row in the dataframe
for _, row in df_lowrisk.iterrows():
    if row.isnull().all():
        continue  # Skip this row if it's entirely blank
    total_cases_low += 1
    for column, text in row.items():  # Iterate through all columns
        if pd.isnull(text):
            continue  # Skip null values
        for keyword in keywords:
            appearances = count_keyword_appearances(str(text), keyword)
            if appearances > 0:
                keyword_counts_low[keyword] += 1

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

print("Summary" + "\n")

#count number of appearances of keywords in different tables
print("-----In New Registration-----" + "\n")
for keyword, count in keyword_counts_new.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Robert-----" + "\n")
for keyword, count in keyword_counts_Rob.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Dominique-----" + "\n")
for keyword, count in keyword_counts_Dom.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Divad-----" + "\n")
for keyword, count in keyword_counts_Divad.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Rachelle-----" + "\n")
for keyword, count in keyword_counts_Rachelle.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Khalid-----" + "\n")
for keyword, count in keyword_counts_Khalid.items():
    print(f"{keyword} found {count}" + "\n")

print("-----SandyHousing-----" + "\n")
for keyword, count in keyword_counts_Sandy.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Incarcerated_waitlist-----" + "\n")
for keyword, count in keyword_counts_incarcerated.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Inactive-----" + "\n")
for keyword, count in keyword_counts_inactive.items():
    print(f"{keyword} found {count}" + "\n")

print("-----Low_risk-----" + "\n")
for keyword, count in keyword_counts_low.items():
    print(f"{keyword} found {count}" + "\n")

print("-------------------------------------------------" + "\n")
# count numbers for requested client questions 
keyword_counts_list = [keyword_counts_new, keyword_counts_Rob, keyword_counts_Dom, keyword_counts_Divad, keyword_counts_Rachelle, keyword_counts_Khalid, keyword_counts_Sandy, keyword_counts_incarcerated, keyword_counts_inactive, keyword_counts_low]

total_counts = {keyword: 0 for keyword in keyword_counts_new}

for counts in keyword_counts_list:
    for keyword, count in counts.items():
        total_counts[keyword] += count

for keyword, total in total_counts.items():
    print(f"The total number of people that ORC helped in {keyword} is {total}" + "\n")

print("-------------------------------------------------" + "\n")

#total number of cases
total_cases = total_cases_new + total_cases_Rob + total_cases_Dom + total_cases_Divad + total_cases_Rachelle + total_cases_Khalid + total_cases_Sandy + total_cases_incarcerated + total_cases_inactive + total_cases_low
print(f"The total number of cases is {total_cases}" + "\n")

print("-------------------------------------------------" + "\n")

#some percentages
for keyword, total in total_counts.items():
    percentage = round(total/float(total_cases) * 100, 5)
    print(f"The percentage of {keyword} is {percentage}%" + "\n")


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

#create a graph for visualization
plt.figure(figsize=(10, 8)) 
plt.bar(list(total_counts.keys()), list(total_counts.values()), color='skyblue')

plt.title('Total Number of Keyword Appearances')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()