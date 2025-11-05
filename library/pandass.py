
import pandas as pd

#Create Series
s = pd.Series([10, 20, 30, 40])
print("1. Series:\n", s)

#Create DataFrame
data = {'Name': ['Pragati', 'Sayali', 'Prjyot'], 'Age': [22, 21, 23]}
df = pd.DataFrame(data)
print("\n2. DataFrame:\n", df)

#Head
print("\n3. Head:\n", df.head())

#Tail
print("\n4. Tail:\n", df.tail())

#Info
print("\n5. Info:")
df.info()

#Describe
print("\n6. Describe:\n", df.describe())

#Select column
print("\n7. Names column:\n", df['Name'])

#Access row
print("\n8. Row using loc:\n", df.loc[0])

#Sort values
sorted_df = df.sort_values(by='Age')
print("\n9. Sorted by Age:\n", sorted_df)

#Handle missing values
df2 = pd.DataFrame({'A': [1, 2, None], 'B': [5, None, 7]})
print("\n10. Original with missing values:\n", df2)
print("\nCheck missing:\n", df2.isnull())
print("\nAfter removing missing:\n", df2.dropna())