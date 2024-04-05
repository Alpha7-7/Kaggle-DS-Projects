import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data into a pandas DataFrame
train_data = pd.read_csv('/Users/AlecChen/Documents/GitHub/Kaggle-DS-Projects/house-prices-advanced-regression-techniques/train.csv')
test_data = pd.read_csv('/Users/AlecChen/Documents/GitHub/Kaggle-DS-Projects/house-prices-advanced-regression-techniques/test.csv')
## EDA Display the first few rows of the dataset
print(train_data.head())

# Get the summary statistics of the dataset
print(train_data.describe())

# Check for missing values
print(train_data.isnull().sum())
print(train_data.columns)