import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

""" TASK2= City Analysis
Identify the city with the highest number of restaurants in the dataset.
Calculate the average rating for restaurants in each city.
Determine the city with the highest average rating. """

# City with highest number of restaurants
top_city = df['city'].value_counts().idxmax()
print("City with highest restaurants:", top_city)

# Average rating per city
avg_rating_city = df.groupby('city')['aggregate_rating'].mean()
print("\nAverage rating by city:\n", avg_rating_city)

# City with highest average rating
best_city = avg_rating_city.idxmax()
print("\nCity with highest average rating:", best_city)
