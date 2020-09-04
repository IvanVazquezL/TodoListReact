# Load the Pandas libraries with alias 'pd'
import pandas as pd
import datetime as dt

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("vgsales.csv")
# Preview the first 5 lines of the loaded data
print(data.head())
print(len(data))

#qUESTION 2
data = data[~data.Name.str.contains('FIFA')]

print(len(data))

#Question 3
#data = data[~(data.Genre.str.contains('Sports') & data.Genre.str.contains('Fighting') & data.Genre.str.contains('Racing') & data.Year <= 1989)]
#data = data[(data.Genre.str.contains('Sports') | data.Genre.str.contains('Fighting') | data.Genre.str.contains('Racing'))]
#data = data[~(data['Year'] > 1989)]
genres = ["Sports","Fighting","Racing"]
years = [0,1989]
# data = data[data.Year > 1989 ]
# print(data)
# print(len(data))
# data = data[(data.Genre.isin(genres) & data.Year.isin(years))]
# print(data)
# data = data[~(data.Genre.isin(genres) & data.Year.isin(years))]
data2 = data[data.Genre.isin(genres)]
data2 = data2[data2.Year <= 1989]
print(data2)
print(len(data2))

print(len(data))

data = data - data2

print(len(data))
