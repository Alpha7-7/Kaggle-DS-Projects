import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the train data into a pandas DataFrame
train_data = pd.read_csv('train.csv')

# Display the first few rows of the dataset
print(train_data.head())

# Get the summary statistics of the dataset
print(train_data.describe())

# Check for missing values
print(train_data.isnull().sum())
