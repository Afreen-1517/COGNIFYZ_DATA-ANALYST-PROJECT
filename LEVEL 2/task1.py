import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

"""TASK1= Restaurant Ratings
Analyze the distribution of aggregate ratings and determine the most common rating range.
Calculate the average number of votes received by restaurants."""

import matplotlib.pyplot as plt

# Rating distribution
df["aggregate_rating"].hist()
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()

# Most common rating range
print("Most common ratings:")
print(df["aggregate_rating"].value_counts().head())

# Average number of votes
print("\nAverage number of Votes received by restaurant:", df["votes"].mean())

