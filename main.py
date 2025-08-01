#importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# data_path=''
# data_name=''

def data_cleaning_master(data_path,data_name):
        
    print("Thank you for giving the details!")

    #Generating random number
    sec=random.randint(1,4)

    #print delay message
    print(f'please wait for {sec} seconds! Checking file path')
    time.sleep(sec)

    # path check
    if not os.path.exists(data_path):
        print("Please enter correct path!")
        return 
    else:
        if data_path.endswith('.csv'):
            print("Dataset is csv!")
            data=pd.read_csv(data_path,encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print("Dataset is excel file!")
            data=pd.read_excel(data_path)

        else:
            print("Unknown file type")
            return
        
    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for {sec} seconds! Checking total cols and rows')
    time.sleep(sec)

    # showing no of records
    print(f'Dataset contains total rows: {data.shape[0]} , total Columns: {data.shape[1]}')

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for {sec} seconds! Checking total duplicates')
    time.sleep(sec)

    # start cleaning
    #checking duplicates
    duplicates=data.duplicated()
    total_duplicate=data.duplicated().sum()

    print(f'Dataset has total duplicate records :{total_duplicate}')

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for {sec} seconds! saving duplicates')
    time.sleep(sec)
    
    #saving the duplicates
    if total_duplicate>0:
        duplicated_records=data[duplicates]
        duplicated_records.to_csv(f'{data_name}_duplicates.csv',index=None)

    #deleting the duplicates
    df=data.drop_duplicates(inplace=True)

    #print delay message
    sec=random.randint(1,10)
    print(f'please wait for {sec} seconds! Checking for missing values')
    time.sleep(sec)

    #find missing values
    total_missing_value= df.isnull().sum().sum()
    missing_value_by_cols=df.isnull().sum()

    print(f'Dataset has Total missing value: {total_missing_value}')
    print(f'Dataset contain missing value by columns {missing_value_by_cols}')

    # dealing with missing values
    #fillna -- int and float
    #dropna -- any object

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for {sec} seconds! cleaning datasets')
    time.sleep(sec)

    columns=df.columns

    for col in columns:
        #filling mean for numeric cols all rows
        if df[col].dtype in (float,int):
            df[col]=df[col].fillna(df[col].mean())
        else:
            # dropping all rows with missing records for a non num col
            df.dropna(subset=col,inplace=True)

    #print delay message
    print(f'please wait for {sec} seconds! Exporting datasets')
    time.sleep(sec)

    # data is cleaned
    print(f"Dataset is cleaned, \n Number of rows:{df.shape[0]}, Number of cols: {df.shape[1]} ")

    #saving the clean dataset
    df.to_csv(f'{data_name}_Clean_data.csv',index=None)
    print("Dataset is saved!")

#call function
if __name__=='__main__':
    print("Welcome to Data Cleaning Master!")
    #ask the path and file name
    data_path=input("Please enter dataset path:")
    data_name=input("Please enter dataset name:")

    #calling the function
    data_cleaning_master(data_path,data_name)