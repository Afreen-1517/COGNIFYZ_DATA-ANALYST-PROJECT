import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

""" TASK2= Cuisine Comibination
Identify the most common combinations of cuisines in the dataset.
Determine if certain cuisine combinations tend to have higher ratings."""

# Most common cuisine combinations
combo_counts = df["cuisines"].value_counts()
print("Top Cuisine Combinations:")
print(combo_counts.head(5))

# Average rating per cuisine combination
combo_rating = df.groupby("cuisines")["aggregate_rating"].mean()
print("\nTop Rated Cuisine Combinations:")
print(combo_rating.sort_values(ascending=False).head(5))
