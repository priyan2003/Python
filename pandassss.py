import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['col1','col2','col3','col4'])
print(df)
df2 = df.to_csv('test1.csv')
df3 = pd.read_csv('test2.csv')
print(df3)
print(df2.head(1))


# df3 = pd.read_clipboard()
# print(df3)
# x = input("Enter file name to read data: ")
# print("Reading data from", x)
# for i in range(0,25):
#     print(i,end=" ")
# print('\n')    
# df2 = pd.read_csv('test2.csv')
# print(df2)
# print(df2.describe())