import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

""" TASK4: Restaurant Chains
Identify if there are any restaurant chains present in the dataset.
Analyze the ratings and popularity of different restaurant chains. """

# Chains are restaurants appearing multiple times
chains = df["restaurant_name"].value_counts()
print("Restaurant Chains:")
print(chains[chains > 1].head(10))

# Average rating for chains
chain_rating = df.groupby("restaurant_name")["aggregate_rating"].mean()
print("\nTop Chains by Rating:")
print(chain_rating.sort_values(ascending=False).head(10))

# Popular chains based on votes
chain_votes = df.groupby("restaurant_name")["votes"].mean()
print("\nTop Chains by Popularity:")
print(chain_votes.sort_values(ascending=False).head(10))
