import pandas as pd
import re
import math
import matplotlib.pyplot as plt 
from datetime import datetime



"""
Version 2.0 of keyword_searcher. In this version, you can find the total number of rows which 
exists any keyword from keywords list, without duplications. This means you can use multiple 
keywords for a single question.
"""


keywords = ['educational', 'education']







def count_keyword_appearances(text, keyword):
    return len(re.findall(keyword, text, re.IGNORECASE))


def get_fiscal_year(date_str):
    date = datetime.strptime(date_str, "%m/%d/%y")
    year = date.year
    if date.month < 7: 
        year -= 1
    return f"FY{year}-{year+1}"








file_new = "cleaned_data/New_registration.csv"
df_new = pd.read_csv(file_new)

df_new = df_new[df_new['Services_Requested_and_Offered'].notna()]

keyword_counts_by_fiscal_year_new = {}
total_cases_new = 0

if "Date_of_Enrollment" in df_new.columns:
    for _, row in df_new.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_new += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_new:
            keyword_counts_by_fiscal_year_new[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_new[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break
       








file_Robert = 'cleaned_data/Robert.csv'
df_Robert = pd.read_csv(file_Robert) 

keyword_counts_by_fiscal_year_Rob = {}
total_cases_Rob = 0

if "Date_of_Enrollment" in df_Robert.columns:
    for _, row in df_Robert.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Rob += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Rob:
            keyword_counts_by_fiscal_year_Rob[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Rob[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break












file_Dom = 'cleaned_data/Dominique.csv'
df_Dom = pd.read_csv(file_Dom) 

keyword_counts_by_fiscal_year_Dom = {}
total_cases_Dom = 0

if "Date_of_Enrollment" in df_Dom.columns:
    for _, row in df_Dom.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Dom += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Dom:
            keyword_counts_by_fiscal_year_Dom[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Dom[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break












file_Divad = 'cleaned_data/Divad.csv'
df_Divad = pd.read_csv(file_Divad) 

keyword_counts_by_fiscal_year_Divad = {}
total_cases_Divad = 0

if "Date_of_Enrollment" in df_Divad.columns:
    for _, row in df_Divad.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Divad += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Divad:
            keyword_counts_by_fiscal_year_Divad[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Divad[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break










file_Rachelle = 'cleaned_data/Rachelle.csv'
df_Rachelle = pd.read_csv(file_Rachelle) 

keyword_counts_by_fiscal_year_Rachelle = {}
total_cases_Rachelle = 0

if "Date_of_Enrollment" in df_Rachelle.columns:
    for _, row in df_Rachelle.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Rachelle += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Rachelle:
            keyword_counts_by_fiscal_year_Rachelle[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Rachelle[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break











file_Khalid = 'cleaned_data/Khalid.csv'
df_Khalid = pd.read_csv(file_Khalid)  

keyword_counts_by_fiscal_year_Khalid = {}
total_cases_Khalid = 0

if "Date_of_Enrollment" in df_Khalid.columns:
    for _, row in df_Khalid.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Khalid += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Khalid:
            keyword_counts_by_fiscal_year_Khalid[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Khalid[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break









file_Sandy = 'cleaned_data/SandyHousing.csv'
df_Sandy = pd.read_csv(file_Sandy)  

keyword_counts_by_fiscal_year_Sandy = {}
total_cases_Sandy = 0

if "Date_of_Enrollment" in df_Sandy.columns:
    for _, row in df_Sandy.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_Sandy += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_Sandy:
            keyword_counts_by_fiscal_year_Sandy[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_Sandy[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break










file_incarcerated = 'cleaned_data/Incarcerated_waitlist.csv'
df_incarcerated = pd.read_csv(file_incarcerated)  

keyword_counts_by_fiscal_year_incarcerated = {}
total_cases_incarcerated = 0

if "Date_of_Enrollment" in df_incarcerated.columns:
    for _, row in df_incarcerated.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_incarcerated += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_incarcerated:
            keyword_counts_by_fiscal_year_incarcerated[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_incarcerated[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break











file_inactive = 'cleaned_data/Inactive.csv'
df_inactive = pd.read_csv(file_inactive)  

keyword_counts_by_fiscal_year_inactive = {}
total_cases_inactive = 0

if "Date_of_Enrollment" in df_inactive.columns:
    for _, row in df_inactive.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_inactive += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_inactive:
            keyword_counts_by_fiscal_year_inactive[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_inactive[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break









file_lowrisk = 'cleaned_data/Low_risk.csv'
df_lowrisk = pd.read_csv(file_lowrisk)  

keyword_counts_by_fiscal_year_lowrisk = {}
total_cases_lowrisk = 0

if "Date_of_Enrollment" in df_lowrisk.columns:
    for _, row in df_lowrisk.iterrows():
       
        date_str = row.get("Date_of_Enrollment")
        if pd.isnull(date_str):
            continue
        total_cases_lowrisk += 1

        fiscal_year = get_fiscal_year(date_str)
        
        if fiscal_year not in keyword_counts_by_fiscal_year_lowrisk:
            keyword_counts_by_fiscal_year_lowrisk[fiscal_year] = 0

        keyword_found = False

        for column, text in row.items():  
            if pd.isnull(text) or column == "Date_of_Enrollment":
                continue 
            for keyword in keywords:
                if count_keyword_appearances(str(text), keyword) > 0:
                    keyword_counts_by_fiscal_year_lowrisk[fiscal_year] += 1
                    keyword_found = True
                    break

            if keyword_found == True:
                break











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
    for fiscal_year, count in data.items():
        print(f"In {fiscal_year}: found {count}\n")











total_counts_by_fiscal_year = {}

for data in datasets.values():
    for fiscal_year, count in data.items():
       
        if fiscal_year not in total_counts_by_fiscal_year:
            total_counts_by_fiscal_year[fiscal_year] = 0

        total_counts_by_fiscal_year[fiscal_year] += count

for fiscal_year, count in total_counts_by_fiscal_year.items():
    print(f"In {fiscal_year}: total number of help is {count}\n")





