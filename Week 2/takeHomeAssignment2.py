# Numpy

import numpy as np

# 1) Define arrays A, B and stack them vertically & horizontally
A = np.array([1, 3, 5, 7, 9])
B = np.array([3, 6, 9, 12, 15])

v_stacked = np.vstack([A, B])      # shape (2, 5)
h_stacked = np.hstack([A, B])      # shape (10,)
print(v_stacked)
print(h_stacked)

# 2) Common elements between A and B (intersection)
common = np.intersect1d(A, B)
print(common)

# 3) Values in A within [5, 10]
in_range = A[(A >= 5) & (A <= 10)]
print(in_range)

# 4) Filter iris_2d rows: petallength (3rd col) > 1.5 AND sepallength (1st col) < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
mask = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
filtered_rows = iris_2d[mask]
print(filtered_rows)


# Pandas

import pandas as pd

# 1) Every 20th row (starting at 0) with columns Manufacturer, Model, Type
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
subset_every_20 = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print(subset_every_20)

# 2) Fill NaNs in Min.Price and Max.Price with their column means
for col in ['Min.Price', 'Max.Price']:
    df[col] = df[col].fillna(df[col].mean())

# verify there are no NaNs left in these two columns
print(df[['Min.Price', 'Max.Price']].isna().sum())

# 3) Rows of a dataframe whose row-sum > 100
rng = np.random.default_rng(0)
df2 = pd.DataFrame(rng.integers(10, 40, 60).reshape(-1, 4), columns=list('ABCD'))
rows_sum_gt_100 = df2[df2.sum(axis=1) > 100]
print(df2.head())
print(rows_sum_gt_100)
