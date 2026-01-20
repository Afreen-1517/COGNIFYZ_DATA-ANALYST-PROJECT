import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

""" TASK4= Online Delivery
Determine the percentage of restaurants that offer online delivery.
Compare the average ratings of restaurants with and without online delivery. """
# Percentage of restaurants offering online delivery
delivery_counts = df['has_online_delivery'].value_counts()

print("Online Delivery Counts:")
print(delivery_counts)

delivery_percent = round((delivery_counts / len(df)) * 100, 2)

print("\nPercentage of Restaurants that offers online delivery:")
print(delivery_percent)

# Compare average ratings
delivery_rating = df.groupby('has_online_delivery')['aggregate_rating'].mean()

print("\nAverage Ratings (Online Delivery vs No Delivery):")
print(delivery_rating)
