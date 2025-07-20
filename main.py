#importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

data_path=''
data_name=''

# path check
if not os.path.exists(data_path):
    print("Please enter correct path!")
else:
    if data_path.endswith('.csv'):
        print("Dataset is csv!")
        data=pd.read_csv(data_path,encoding_errors='ignore')

    elif data_path.endswith('.xlsx'):
        print("Dataset is excel file!")
        data=pd.read_excel(data_path,encoding_errors='ignore')

    else:
        print("Unknown file type")


# showing no of records
print(f'Dataset contains total rows: {data.shape[0]} , total Columns: {data.shape[1]}')

# start cleaning
duplicates=data.duplicated()
total_duplicate=data.duplicated().sum()

print(f'Dataset has total duplicate records :{total_duplicate}')

#saving the duplicates
if total_duplicate>0:
    duplicated_records=data[duplicates]
    duplicated_records.to_csv(f'{data_name}_duplicates.csv',index=None)

#deleting the duplicates
df=data.drop_duplicates(inplace=True)

#find missing values
total_missing_value= df.isnull().sum().sum()
missing_value_by_cols=df.isnull().sum()

print(f'Dataset has Total missing value: {total_missing_value}')
print(f'Dataset contain missing value by columns {missing_value_by_cols}')

# dealing with missing values

