import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

""" TASK3= Price Range Distribution
Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
Calculate the percentage of restaurants in each price range category. """

# Count restaurants by price range
price_counts = df['price_range'].value_counts()

print("Restaurants in each price range:")
print(price_counts)

# Percentage calculation
price_percent = round((price_counts / len(df)) * 100, 2)

print("\nPercentage of restaurants in each price range:")
print(price_percent)

# Plot bar chart
import matplotlib.pyplot as plt

price_counts.sort_index().plot(kind='bar')
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution ")
plt.show()
