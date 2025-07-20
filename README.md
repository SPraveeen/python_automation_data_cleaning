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
