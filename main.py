import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('911.csv')

# top 5 Zip Codes
maxZip = df['zip'].value_counts().head(5)
print('The top 5 Zip codes are:\n', maxZip)

# top townships
maxTwp = df['twp'].value_counts().head()
print('The top 5 townships are:\n', maxTwp)

print(df['title'].count())

# categorize reasons/department into a new Series of the DataFrame


def reason(str):
    if 'EMS' in str:
        return 'EMS'
    elif 'Traffic' in str:
        return 'Traffic'
    else:
        return 'Injury'


# graphical representation of reasons
df['Reason'] = df['title'].apply(lambda x: reason(x))
reasonCount = df['Reason'].value_counts()
print('Counts of reasons:\n', reasonCount)
sns.countplot(df['Reason'])

plt.show()
