import pandas

file = pandas.read_csv("country_data.csv")

print("---------Country data---------")
print(file)
print(file.info())
print(file.describe()) #print(df.describe()) in canvas lecture


iris = pandas.read_csv("iris.csv")

print("---------Iris data---------")
print(iris)
print(iris.info())
print(iris.describe())


diab = pandas.read_csv("diab_data.csv")

print("---------Diab data---------")
print(diab)
print(diab.info())
print(diab.describe())


hous = pandas.read_csv("housing_data.csv")

print("---------Housing data---------")
print(hous)
print(hous.info())
print(hous.describe())

column_names = ["A", "B", "C"]
hous = pandas.read_csv("housing_data.csv", names = column_names)


ins = pandas.read_csv("insurance_data.csv", skiprows=(6))

print("---------Insurance Data---------")
print(ins)
print(ins.info())
print(ins.describe())

# -------Sorting Data-------

B11 = 30
B10 = 40
B9 = 30
B8 = 49
B7 = 22
B6 = 35
B5 = 22
B4 = 46
B3 = 29
B2 = 25
B1 = 39

print(B1)
print(B2)


# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[5])
print(age[10])

# This will give an error as there is no value at index 11
#print(age[11])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))

avg = sum(age)/len(age)
print(avg)

# Storing Text
C2 = "M"
C3 = "M"
C4 = "F"

print(C2)
print(C3)
print(C4)

# gender list
gender = ["M", "M","F","M","F","F","F","M","M","F","M"]

print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])


# country list
country = ["South Africa","Botswana","South Africa","South Africa"
           ,"Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt"
           ,"Sudan"]

print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
'''
Things to do with lists

Print all the items in the list using [:]
We can add items to the end of the list using append()
Add items at specific positions using insert()
Remove an item from the list using the remove() function
Check how many variables are in the list using the len()
Print a range of values using [start:end] – just like in excel!
'''

my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])

# Dictionaries
'''
A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are also known as associative arrays or hash maps. They are similar to lists, but instead of using integer indices to access elements, you use keys. It is an unordered data type that is structured using keys and values and is defined with curly brackets {}. Where keys are like the column names and values are the lists of data.
'''
d = {'key1': 'value1', 'key2': 'value2'}

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'

# Data frame
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

print(df)


# Accessing specific columns
print(df['age'])
print(df['gender'])


# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering data
print(df[df['age'] > 30])


# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns


# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)














