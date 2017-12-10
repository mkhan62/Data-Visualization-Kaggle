import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('911.csv')

# top 5 Zip Codes
maxZip = df['zip'].value_counts().head(5)
# print('The top 5 Zip codes are:\n', maxZip)

# top townships
maxTwp = df['twp'].value_counts().head(5)
# print('The top 5 townships are:\n', maxTwp)

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
# print('Counts of reasons:\n', reasonCount)
# sns.countplot(df['Reason'])

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].dt.weekday_name
df['Date'] = df['timeStamp'].apply(lambda x: x.date())

# sns.countplot(df['Day of Week'], hue=df['Reason'], palette='coolwarm')
# sns.countplot(df['Month'], hue=df['Reason'], palette='coolwarm')

byMonth = df[df['Reason'] == 'EMS'].groupby('Month').count()
# sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
byDate = df.groupby('Date').count().reset_index()

# byDate.plot.line(x='Date', y='lat')
# plt.tight_layout()

heatMapFrame1 = df.groupby(['Day of Week', 'Hour']).count()['lat'].unstack(level=-1)
heatMapFrame2 = df.groupby(['Day of Week', 'Month']).count()['lat'].unstack(level=-1)
sns.clustermap(heatMapFrame2, linewidths=1, linecolor='white', cmap='Blues')
plt.tight_layout()
plt.show()



