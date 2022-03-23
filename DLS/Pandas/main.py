import pandas as pd
import numpy as np


# pd.Series - one-dimensional table with data

some = [1, 2, 3]
series = pd.Series(some)
print(series)

index = ['1st day', '2nd day', '3rd day']
series = pd.Series(some, index=index)
print(series)
print(series[0])
print(series[1:3])
print(series['3rd day'])
print(series['1st day':'2nd day'])

date = pd.date_range('20220101', periods=10)
series = pd.Series(np.random.rand(10), index=date)
print(series)
print(series > 0.5)
print(series + 100)
print(np.exp(series))

series_1 = pd.Series(np.random.randint(0, 10, 5))
series_2 = pd.Series(np.random.randint(0, 10, 5))
print(series_1 + series_2)


# pd.DataFrame - 2D data table

some = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
        'three': pd.Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'])}
dataframe = pd.DataFrame(some)
print(dataframe)
print(dataframe.columns)
print(dataframe.one)
print(dataframe['one'])
print(dataframe[['one', 'two']])
# Don`t do it!
# print(dataframe[1]) 
print(dataframe.iloc[1:3, :2])
print(dataframe.loc[1:3], ['one', 'two'])

four = [1, 2, 3, 4, 5]
dataframe['four'] = four
print(dataframe)
print(dataframe['four'] * 10)

