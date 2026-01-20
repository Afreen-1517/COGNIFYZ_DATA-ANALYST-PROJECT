import pandas as pd
df=pd.read_csv("dataset.csv")
print(df.head())
df.info()
print(df.describe(include="all"))
print(df.isnull().sum())
# Fill missing cuisines based on city mode
df["Cuisines"]=df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
print("\n After transforming null values: \n")
print(df.isnull().sum())
# Rename columns for easy use
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
print(df.columns)


""" TASK1= Top Cuisines
Determine the top three most common cuisines in the dataset.
Calculate  the percentage of restaurants that serve each of the topcuisines. """

# Split cuisines column because multiple cuisines are comma separated
cuisines = df['cuisines'].dropna().str.split(', ')

# Flatten list and count cuisinesa
from collections import Counter
cuisine_list = [c for sub in cuisines for c in sub]
top3 = Counter(cuisine_list).most_common(3)

print("\n Top 3 cuisines:")
print(top3)

total = len(df)
print("\n The percentage of restaurants that serve each of top cuisines: ") 
for cuisines, count in top3:
    print(f"{cuisines}: {round((count/total)*100,2)}% restaurants")
