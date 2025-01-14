# -*- coding: utf-8 -*-
"""CIE EXAM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16LwOv5C9Htw6sC380shDShYGWo9Bix2L
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/mtcars (3).csv")

plt.figure(figsize=(8, 6))
plt.hist(df['mpg'], bins=10, edgecolor='black')
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of MPG')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.scatterplot(x='wt', y='mpg', data=df)
plt.xlabel('Weight')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Scatter Plot of Weight vs MPG')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/content/mtcars.csv')
plt.figure(figsize = (8, 6))
sns.barplot(x='wt', y='am',data=df)
plt.xlabel('Weight')
plt.ylabel('Count of Transmission Types')
plt.title("Bar Plot: Frequency Distribution of Transmission Types")
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 5))
plt.title('Box Plot of Miles')
sns.boxplot(x=df['mpg'])
plt.xlabel('Miles per gallon  per gallon (mpg)')
plt.grid(True)
plt.show()
summary = df['mpg'].describe()
print(summary[['min','25%', '50%', '75%','max' ]])