# Data Cleaning Master - Python Application
## Project Overview
<img src='https://github.com/SPraveeen/python_automation_data_cleaning/blob/main/img.webp'/>
The Data Cleaning Master is a **Python application** designed to efficiently clean datasets by handling duplicates, missing values, and providing cleaned output within seconds. The application is user-friendly, highly performant, and has been tested on various datasets, ensuring smooth execution and accuracy.

This application can handle datasets with thousands of rows and quickly clean them without errors. It keeps a backup of duplicate records, replaces missing numeric values with column means, and drops rows with missing non-numeric values. This makes it an excellent tool for data pre-processing in data analysis workflows.

## Objectives
### The key objectives of this project are:

- Load and clean datasets in various formats (CSV and Excel).
- Identify and remove duplicate records, while keeping a backup of these duplicates.
- Handle missing values:
- For numeric columns: replace missing values with the column's mean.
- For non-numeric columns: remove rows containing missing values.
- Save the cleaned dataset and provide access to both the cleaned data and duplicate records.

## Project Requirements
- Python 3.x
- Pandas
- Numpy
- Openpyxl
- Xlrd
- OS library
- Jupyter Notebook (for testing)

## Step-by-Step Process
1. Input and File Verification
- The application begins by asking the user for the dataset path and dataset name.
- It verifies if the path is valid and checks whether the file is in a supported format (CSV or Excel).
2. Duplicate Detection and Removal
- The application checks for duplicate records in the dataset.
- Duplicate records are saved as a separate file named {dataset_name}_duplicates.csv.
Duplicate rows are then removed from the main dataset.
3. Handling Missing Values
- The application checks for missing values in the dataset.
- For numeric columns (integer or float), missing values are replaced by the column’s mean.
- For non-numeric columns, rows containing missing values are dropped.
4. Exporting Clean Data
- Once cleaned, the dataset is saved as {dataset_name}_Clean_data.csv, and a message confirming successful cleaning is displayed.
5. Multiple Testing & Performance Tuning
- The application has been tested with more than 5 different datasets, each containing over 10,000 rows. It consistently cleaned datasets in a matter of seconds, without errors.
- The program was also tested using Jupyter Notebook, where it performed flawlessly, allowing easy integration with data science workflows.
## Key Features
- Fast & Efficient: Cleans large datasets (10k+ rows) in seconds.
Duplicate Backup: Keeps a backup of all duplicate records before removing them.
- Missing Values Handling: Automatically fills missing numeric values and drops rows with missing non-numeric values.
- User-friendly Prompts: Guides the user step by step with appropriate messages and delay prompts.
- Multiple Formats Supported: Handles CSV and Excel files seamlessly.
## Usage
- Run the application using a Python environment.
- Input the dataset path and name when prompted.
- The application will automatically clean the dataset and save the results.

```
python data_cleaning_master.py
```

## Example of Execution
```
Welcome to Data Cleaning Master!
Please enter dataset path: /usr/Dekstop/amazon.csv
Please enter dataset name: amazon_sales_data
```
## Expected output:

- Duplicate records saved as: sales_data_duplicates.csv
- Cleaned data saved as: sales_data_Clean_data.csv
## Final Thoughts
The Data Cleaning Master is an efficient tool for data pre-processing. Its ability to handle large datasets, clean data accurately, and save duplicates for further inspection makes it ideal for any data science or data analysis project.

