import pandas as pd
import re
import math
import matplotlib.pyplot as plt 
from datetime import datetime


"""
    This is the list of keywords, and each keyword should represents a question/sub-question. Cannot use multiple keywords for the same queston.
    To use the codes, ONLY change keywords here. 
    |
    |
    |
   \ /
    V
    
"""
keywords = ["cori"] 


#NO NEED TO CHANGE CODES BELOW
"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Two Helper Functions."""

# Function to count appearances of a keyword in a row
def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))

# Helper function to determine the fiscal year from a date
def get_fiscal_year(date_str):
    date = datetime.strptime(date_str, "%m/%d/%y")
    year = date.year
    if date.month < 7:  # If before July, it belongs to the previous fiscal year
        year -= 1
    return f"FY{year}-{year+1}"


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""new registration"""


file_new = 'cleaned_data/New_registration.csv'
df_new = pd.read_csv(file_new)

# Filter out rows where 'Services Requested and Offered' is blank
df_new = df_new[df_new['Services_Requested_and_Offered'].notna()]

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_new = {}

# Initialize counter for total number of cases
total_cases_new = 0

if "Date_of_Enrollment" in df_new.columns:
    for _, row in df_new.iterrows():
        if row.isnull().all():
            continue
        total_cases_new += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_new:
            keyword_counts_by_fiscal_year_new[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_new[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Robert"""


file_Robert = 'cleaned_data/Robert.csv'
df_Robert = pd.read_csv(file_Robert) 

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Rob = {}

# Initialize counter for total number of cases
total_cases_Rob = 0

if "Date_of_Enrollment" in df_Robert.columns:
    for _, row in df_Robert.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Rob += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Rob:
            keyword_counts_by_fiscal_year_Rob[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Rob[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Dominique"""


file_Dom = 'cleaned_data/Dominique.csv'
df_Dom = pd.read_csv(file_Dom)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Dom = {}

# Initialize counter for total number of cases
total_cases_Dom = 0

if "Date_of_Enrollment" in df_Dom.columns:
    for _, row in df_Dom.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Dom += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Dom:
            keyword_counts_by_fiscal_year_Dom[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Dom[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Divad"""


file_Divad = 'cleaned_data/Divad.csv'
df_Divad = pd.read_csv(file_Divad)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Divad = {}

# Initialize counter for total number of cases
total_cases_Divad = 0

if "Date_of_Enrollment" in df_Divad.columns:
    for _, row in df_Divad.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Divad += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Divad:
            keyword_counts_by_fiscal_year_Divad[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Divad[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Rachelle"""


file_Rachelle = 'cleaned_data/Rachelle.csv'
df_Rachelle = pd.read_csv(file_Rachelle)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Rachelle = {}

# Initialize counter for total number of cases
total_cases_Rachelle = 0

if "Date_of_Enrollment" in df_Rachelle.columns:
    for _, row in df_Rachelle.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Rachelle += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Rachelle:
            keyword_counts_by_fiscal_year_Rachelle[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Rachelle[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Khalid"""


file_Khalid = 'cleaned_data/Khalid.csv'
df_Khalid = pd.read_csv(file_Khalid) 

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Khalid = {}

# Initialize counter for total number of cases
total_cases_Khalid = 0

if "Date_of_Enrollment" in df_Khalid.columns:
    for _, row in df_Khalid.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Khalid += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Khalid:
            keyword_counts_by_fiscal_year_Khalid[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Khalid[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""SandyHousing"""


file_Sandy = 'cleaned_data/SandyHousing.csv'
df_Sandy = pd.read_csv(file_Sandy)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_Sandy = {}

# Initialize counter for total number of cases
total_cases_Sandy = 0

if "Date_of_Enrollment" in df_Sandy.columns:
    for _, row in df_Sandy.iterrows():
        if row.isnull().all():
            continue  
        total_cases_Sandy += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_Sandy:
            keyword_counts_by_fiscal_year_Sandy[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_Sandy[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Incarcerated_waitlist"""


file_incarcerated = 'cleaned_data/Incarcerated_waitlist.csv'
df_incarcerated = pd.read_csv(file_incarcerated)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_incarcerated = {}

# Initialize counter for total number of cases
total_cases_incarcerated = 0

if "Date_of_Enrollment" in df_incarcerated.columns:
    for _, row in df_incarcerated.iterrows():
        if row.isnull().all():
            continue  
        total_cases_incarcerated += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_incarcerated:
            keyword_counts_by_fiscal_year_incarcerated[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_incarcerated[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Inactive"""


file_inactive = 'cleaned_data/Inactive.csv'
df_inactive = pd.read_csv(file_inactive)

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_inactive = {}

# Initialize counter for total number of cases
total_cases_inactive = 0

if "Date_of_Enrollment" in df_inactive.columns:
    for _, row in df_inactive.iterrows():
        if row.isnull().all():
            continue  
        total_cases_inactive += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_inactive:
            keyword_counts_by_fiscal_year_inactive[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_inactive[fiscal_year][keyword] += 1


"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""Low_risk"""


file_lowrisk = 'cleaned_data/Low_risk.csv'
df_lowrisk = pd.read_csv(file_lowrisk) 

# Initialize a dictionary to count appearances
keyword_counts_by_fiscal_year_lowrisk = {}

# Initialize counter for total number of cases
total_cases_lowrisk = 0

if "Date_of_Enrollment" in df_lowrisk.columns:
    for _, row in df_lowrisk.iterrows():
        if row.isnull().all():
            continue  
        total_cases_lowrisk += 1
        date_str = row["Date_of_Enrollment"]
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
        if fiscal_year not in keyword_counts_by_fiscal_year_lowrisk:
            keyword_counts_by_fiscal_year_lowrisk[fiscal_year] = {keyword: 0 for keyword in keywords}

        for column, text in row.items():  # Iterate through all columns
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue
            for keyword in keywords:
                appearances = count_keyword_appearances(str(text), keyword)
                if appearances > 0:
                    keyword_counts_by_fiscal_year_lowrisk[fiscal_year][keyword] += 1

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""

print("Summary" + "\n")

datasets = {
    "New Registration": keyword_counts_by_fiscal_year_new,
    "Robert": keyword_counts_by_fiscal_year_Rob,
    "Dominique": keyword_counts_by_fiscal_year_Dom,  
    "Divad": keyword_counts_by_fiscal_year_Divad,  
    "Rachelle": keyword_counts_by_fiscal_year_Rachelle,  
    "Khalid": keyword_counts_by_fiscal_year_Khalid,  
    "SandyHousing": keyword_counts_by_fiscal_year_Sandy,  
    "Incarcerated_waitlist": keyword_counts_by_fiscal_year_incarcerated,  
    "Inactive": keyword_counts_by_fiscal_year_inactive,  
    "Low_risk": keyword_counts_by_fiscal_year_lowrisk
}

for dataset_name, data in datasets.items():
    print(f"-----------------{dataset_name}----------------\n")
    for fiscal_year, counts in data.items():
        print(f"In {fiscal_year}:\n")  # Indicate the fiscal year
        for keyword, count in counts.items():
            print(f"{keyword} found {count}\n")


print("--------------------------------------------------------------------------------" + "\n")
# count numbers for requested client questions in fiscal year format
total_counts_by_fiscal_year = {}

# Iterate through each dataset's fiscal year data
for data in datasets.values():
    for fiscal_year, counts in data.items():
       
        if fiscal_year not in total_counts_by_fiscal_year:
            total_counts_by_fiscal_year[fiscal_year] = {keyword: 0 for keyword in keywords}
        
        # Add the counts from this dataset and fiscal year to the total
        for keyword, count in counts.items():
            total_counts_by_fiscal_year[fiscal_year][keyword] += count

for fiscal_year, counts in total_counts_by_fiscal_year.items():
    print(f"In {fiscal_year}:\n")
    for keyword, total in counts.items():
        print(f"The total number of people that ORC helped in {keyword} is {total}\n")

print("--------------------------------------------------------------------------------" + "\n")

#total number of cases (grand total)
total_cases = total_cases_new + total_cases_Rob + total_cases_Dom + total_cases_Divad + total_cases_Rachelle + total_cases_Khalid + total_cases_Sandy + total_cases_incarcerated + total_cases_inactive + total_cases_lowrisk
print(f"The total number of cases (grand total) is {total_cases}" + "\n")

print("--------------------------------------------------------------------------------" + "\n")

#some percentages in fiscal year format
total_cases_by_fiscal_year = {}

datasets = [df_new, df_Robert, df_Dom, df_Divad, df_Rachelle, df_Khalid, df_Sandy, df_incarcerated, df_inactive, df_lowrisk]

for dataset in datasets:
    for _, row in dataset.iterrows():
        date_str = row.get('Date_of_Enrollment')
        # Check if 'Date_of_Enrollment' is not blank and valid
        if pd.notnull(date_str):
            fiscal_year = get_fiscal_year(date_str)
            if fiscal_year not in total_cases_by_fiscal_year:
                total_cases_by_fiscal_year[fiscal_year] = 0
            total_cases_by_fiscal_year[fiscal_year] += 1

for fiscal_year, counts in total_counts_by_fiscal_year.items():
    print(f"In {fiscal_year}:\n")
    total_cases = total_cases_by_fiscal_year.get(fiscal_year, 0)  # Use .get() to default to 0 if the fiscal year isn't found
    if total_cases > 0:  
        print(f"The total number of cases in {fiscal_year} is {total_cases}\n")
        for keyword in keywords:
            total = counts.get(keyword, 0)  # Get the count for the keyword, defaulting to 0
            percentage = (total / float(total_cases)) * 100
            print(f"The percentage of {keyword} in {fiscal_year} is {percentage:.2f}%\n")
    else:
        print(f"No cases found for {fiscal_year}.\n")

"""-------------------------------------------------------------------------------------------------------------------------------------------------------"""
#create graphs in fiscal year format for visualization
all_keywords = set()
for counts in total_counts_by_fiscal_year.values():
    all_keywords.update(counts.keys())

if len(all_keywords) == 1:
    # only one keyword, plot it across all fiscal years
    single_keyword = all_keywords.pop()
    fiscal_years = list(total_counts_by_fiscal_year.keys())
    keyword_counts_over_time = [total_counts_by_fiscal_year[year].get(single_keyword, 0) for year in fiscal_years]

    plt.figure(figsize=(10, 8))
    bars = plt.bar(fiscal_years, keyword_counts_over_time, color='skyblue', width=0.3)
    
    plt.title(f'Total Appearances of {single_keyword} Over Fiscal Years')
    plt.xlabel('Fiscal Years')
    plt.ylabel('Counts')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
else:
    # multiple keywords
    for fiscal_year, counts in total_counts_by_fiscal_year.items():
        plt.figure(figsize=(10, 8))
        keywords = list(counts.keys())
        keyword_counts = list(counts.values())
        
        bar_width = len(keywords)/10
        bars = plt.bar(keywords, keyword_counts, color='skyblue', width=bar_width)

        plt.title(f'Total Number of Keyword Appearances in {fiscal_year}')
        plt.xlabel('Keywords')
        plt.ylabel('Counts')
        plt.xticks(rotation=45, ha="right")

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
