import pandas as pd

df = pd.read_csv("data_02/country_data_index.csv")

df_1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df_1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, names = column_names)

df_2 = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

df_3 = pd.read_excel("data_02/residentdoctors.xlsx")

df_4 = pd.read_json("data_02/student_data.json")

'''
pandas readcsv functions
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.readcsv.html
'''

# =============================================================================
# CSV with index already included
df_5 = pd.read_csv("data_02/country_data_index.csv", index_col=(0))
'''
This will read the CSV file and use the first column as the index, preventing the appearance of the "Unnamed: 0" column in your DataFrame.
'''
# =============================================================================


# =============================================================================
# Skip Rows
df_6 = pd.read_csv("data_02/insurance_data.csv", skiprows=(5))
# =============================================================================


# =============================================================================
# Column Headings
column_names = ["duration", "pulse", "max_pulse", "calories"]

df_7 = pd.read_csv("data_02/patient_data.csv", header=(None), names=column_names)
# =============================================================================


# =============================================================================
# Unique Delimiter
df_8 = pd.read_csv("data_02/Geospatial Data.txt", sep=";")
# =============================================================================


# =============================================================================
# Inconsistent Data Types & Names
df_9 = pd.read_excel("data_02/residentdoctors.xlsx")

'''
Some column headings are snake case and other all caps
AGEDIST has numbers with text
MARITULSTATUS has text fields
'''

# Step 1: Extract the lower end of the age range (digits only)
df_9['LOWER_AGE'] = df_9['AGEDIST'].str.extract('(\d+)-')

'''
Pseudo-code: 
1. Search for a number followed by a hyphen like "30-" 
2. If you find that number, extract the number and ignore the hyphen 
3. Put it in a new column called LOWER_AGE

Then convert that number to from string to integer, a whole number.

This step uses "str.extract()" to capture one or more digits from the 'AGEDIST' column.
When you use df['AGEDIST'].str.extract('(\d+)-'), it applies this regular expression pattern to each element in the 'AGEDIST' column.

Regular expressions (regex or regexp) are sequences of characters that define a search pattern. It extracts the portion of the string that matches the pattern, which is the one or more consecutive digits before the hyphen in the age range. We won't go over regular expressions much, this was just a demonstration to show you different possibilitles.
'''

# Step 2: Convert the new column to float
df_9['LOWER_AGE'] = df_9['LOWER_AGE'].astype(int)

'''
Pseudo-code: 
1. Convert all the data to integers 
2. Store that value back into LOWER_AGE column

After extracting the digits, this step converts the resulting column to floating-point numbers using astype(float). Without this conversion, the extracted values would be treated as strings, and any subsequent numeric operations or analysis would not work as expected.
'''

# Working with Dates
df_10 = pd.read_csv("data_02/time_series_data.csv")

# Convert the 'Date' column to datetime
df_10['Date'] = pd.to_datetime(df_10['Date'])

'''
if your date string is in the "DD-MM-YYYY" format, you would specify the format like this:
df_10['Date'] = pd.to_datetime(df_10['Date'], format='%d-%m-%Y')
'''

# Split the 'Date' column into separate columns for year, month, and day
df_10['Year'] = df_10['Date'].dt.year
df_10['Month'] = df_10['Date'].dt.month
df_10['Day'] = df_10['Date'].dt.day
# =============================================================================


# =============================================================================
# NANs and Wrong Formats
df_11 = pd.read_csv('data_02/patient_data_dates.csv')

# Allows you to see all rows
pd.set_option('display.max_rows',None)

#print(df_11)

'''
Now you will notice the following:

1.The data set has an index column that is redundant
2.The data set contains some empty cells or NaNs (“Date” in row 22, and “Calories” in row 18 and 28, “Maxpulse” in row 1).
3.The data set contains wrong format (“Date” in row 26).
4.The data set contains wrong data (“Duration” in row 7 and 13).
5.The data set contains duplicates (row 11 and 12).
'''
# 1. Remove the columns
df_11.drop(['Index'],inplace=True,axis=1)

'''
When inplace=True, it means that the changes made by the fillna operation will be applied directly to the original DataFrame (df_11 in this case), and it will not return a new DataFrame. The inplace parameter modifies the DataFrame in place, without the need to assign the result back to a variable.
'''

# 2. Replace Empty Values - Using fillna
x = df_11["Calories"].mean()
df_11["Calories"].fillna(x, inplace=True)

'''
The fillna() method allows us to replace empty cells with a value. A common way to replace empty cells, is to calculate the mean (average), median (middle) or mode (most frequent) value of the column.
'''

# Wrong Date Format – Convert with to_datetime()
'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data. To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format. In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the ‘Date’ column should be a string that represents a date. The best way to fix the date is to convert it a versatile date time format unique to Pandas using to_datetime():
'''

df_11['Date'] = pd.to_datetime(df_11['Date'])
'''
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
5         60 2020-12-06    102       127    300.00
6         60 2020-12-07    110       136    374.00
7        450 2020-12-08    104       134    253.30
8         30 2020-12-09    109       133    195.10
9         60 2020-12-10     98       124    269.00
10        60 2020-12-11    103       147    329.30
11        60 2020-12-12    100       120    250.70
12        60 2020-12-12    100       120    250.70
13        60 2020-12-13    106       128    345.30
14        60 2020-12-14    104       132    379.30
15        60 2020-12-15     98       123    275.00
16        60 2020-12-16     98       120    215.20
17        60 2020-12-17    100       120    300.00
18        45 2020-12-18     90       112    304.68
19        60 2020-12-19    103       123    323.00
20        45 2020-12-20     97       125    243.00
21        60 2020-12-21    108       131    364.20
22        45        NaT    100       119    282.00
23        60 2020-12-23    130       101    300.00
24        45 2020-12-24    105       132    246.00
25        60 2020-12-25    102       126    334.50
26        60 2020-12-26    100       120    250.00
27        60 2020-12-27     92       118    241.00
28        60 2020-12-28    103       132    304.68
29        60 2020-12-29    100       132    280.00
30        60 2020-12-30    102       129    380.30
31        60 2020-12-31     92       115    243.00



NaT(Noa a Time) an empy value
'''
# Removing Empty Cells – Using dropna
'''
By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument. The dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame. 
You will also need to reset the index with df.reset_index(drop=True) as if you remove a row, the row numbers will not be consecutive:
'''
df_11.dropna(inplace=True)
df_11 = df_11.reset_index(drop=True)
'''
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
5         60 2020-12-06    102       127    300.00
6         60 2020-12-07    110       136    374.00
7        450 2020-12-08    104       134    253.30
8         30 2020-12-09    109       133    195.10
9         60 2020-12-10     98       124    269.00
10        60 2020-12-11    103       147    329.30
11        60 2020-12-12    100       120    250.70
12        60 2020-12-12    100       120    250.70
13        60 2020-12-13    106       128    345.30
14        60 2020-12-14    104       132    379.30
15        60 2020-12-15     98       123    275.00
16        60 2020-12-16     98       120    215.20
17        60 2020-12-17    100       120    300.00
18        45 2020-12-18     90       112    304.68
19        60 2020-12-19    103       123    323.00
20        45 2020-12-20     97       125    243.00
21        60 2020-12-21    108       131    364.20
22        60 2020-12-23    130       101    300.00
23        45 2020-12-24    105       132    246.00
24        60 2020-12-25    102       126    334.50
25        60 2020-12-26    100       120    250.00
26        60 2020-12-27     92       118    241.00
27        60 2020-12-28    103       132    304.68
28        60 2020-12-29    100       132    280.00
29        60 2020-12-30    102       129    380.30
30        60 2020-12-31     92       115    243.00
'''

# Wrong Data – Replace and Remove Rows
'''
If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
It doesn’t have to be wrong, but taking in consideration that this is the data set of someone’s workout sessions, we conclude with the fact that this person did not work out in 450 minutes.
In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7 with
'''
df_11.loc[7, 'Duration'] = 45
'''
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
5         60 2020-12-06    102       127    300.00
6         60 2020-12-07    110       136    374.00
7         45 2020-12-08    104       134    253.30
8         30 2020-12-09    109       133    195.10
9         60 2020-12-10     98       124    269.00
10        60 2020-12-11    103       147    329.30
11        60 2020-12-12    100       120    250.70
12        60 2020-12-12    100       120    250.70
13        60 2020-12-13    106       128    345.30
.
.
.
'''

# Removing Duplicates – Using drop_duplicates()
'''
By taking a look at our test data set, we can assume that row 11 and 12 are duplicates. To discover duplicates, we can use the duplicated() method. The duplicated() method returns a Boolean values for each row. To remove the duplicates use drop_duplicates() method:
'''
df_11.drop_duplicates(inplace=True)
df_11 = df_11.reset_index(drop=True)
'''
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130    409.10
1         60 2020-12-02    117       145    479.00
2         60 2020-12-03    103       135    340.00
3         45 2020-12-04    109       175    282.40
4         45 2020-12-05    117       148    406.00
5         60 2020-12-06    102       127    300.00
6         60 2020-12-07    110       136    374.00
7         45 2020-12-08    104       134    253.30
8         30 2020-12-09    109       133    195.10
9         60 2020-12-10     98       124    269.00
10        60 2020-12-11    103       147    329.30
11        60 2020-12-12    100       120    250.70
12        60 2020-12-13    106       128    345.30
13        60 2020-12-14    104       132    379.30
.
.
.
'''
# =============================================================================


# =============================================================================
# Applying Data Transformations
'''
Aggregate data using groupby in pandas
Append and merge datasets using different join types
Filter and manipulate data to create new variables.
'''

# Aggregation
grouped = df_1.groupby('class')

df_1['sepal_length_sq'] = df_1['sepal_length']**2

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Display the results
print("Mean of Sepal Length Squared:")
print(mean_squared_values)

print("\nSum of Sepal Length Squared:")
print(sum_squared_values)

print("\nCount of Sepal Length Squared:")
print(count_squared_values)

# Append & Merge
df_12 = pd.read_csv("data_02/person_split1.csv")
df_13 = pd.read_csv("data_02/person_split2.csv")

# Concatenate the dataframes
'''
Appending two data sets together that have the same column names. For example "personsplit1.csv" and "personsplit2.csv:
'''
df_14 = pd.concat([df_12, df_13], ignore_index=True)

'''
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
Merge two datasets together. They are related by the "id" column. We can do that with the following code:
'''
df_15 = pd.read_csv('data_02/person_education.csv')
df_16 = pd.read_csv('data_02/person_work.csv')

## inner join
df_merge_inner = pd.merge(df_15,df_16, on='id')
'''
An inner join returns only the rows where there is a match in both dataframes on the specified "on" column (in this case, the "id" column). If there is no match, the row is excluded from the result.
'''
## outer join
df_merge_outer = pd.merge(df_15, df_16, on='id', how='outer')
'''
An outer join returns all the rows from both dataframes. If there is no match for a row in either dataframe, the missing values will be filled with NaNs. Left and Right Joins are possible too.
'''

# Filtering
# Filter data for females (class == 'Iris-versicolor')
iris_versicolor = df_1[df_1['class'] == 'Iris-versicolor']
'''
When we want to do check for a comparison we use double equals "==" not a single equals sign "="
'''

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()

'''
There is also a better way to label the "class" column since the word "Iris-" is redundant. We can remove it in the following way:
'''
df_1['class'] = df_1['class'].str.replace('Iris-','')

# Apply the square to sepal length using a lambda function
df_17 = pd.read_csv("data_02/iris.csv")

df_17['sepal_length_sq'] = df_17['sepal_length'].apply(lambda x: x**2)
'''
The .apply(lambda x: x**2) part is used to apply a function to each element in the selected 'sepallength' column. In this case, a lambda function is used. The lambda function takes an input parameter x (each individual sepallength value) and squares it.
'''
df_17['class'] = df_17['class'].str.replace('Iris-','')
# =============================================================================

# =============================================================================
# Load
'''
It is always useful to export the data after you have cleaned and performed the transformations. This can be done various formats. Note, we are outputting the files to a new folder, which we will need to create first.
'''
## CSV
df_17.to_csv("data_02/output/iris_data_cleaned.csv")

'''If you don't want the Pandas index column you can specify:'''
df_17.to_csv("data_02/output/iris_data_cleaned.csv", index=False)

'''
Excel
df.to_excel("data_02/output/iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

JSON
df.to_json("data_02/output/iris_data_cleaned.json", orient='records')
'''
# =============================================================================















