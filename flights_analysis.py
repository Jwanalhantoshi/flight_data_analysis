# ===============================
# 1. Import Libraries
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully\n")


# ===============================
# 2. Load Dataset
# ===============================
 

url = "https://rcs.bu.edu/examples/python/DataAnalysis/flights.csv"
df = pd.read_csv(url)


# ===============================
# 3. Explore the Dataset
# ===============================

print(df.head(10))
  
print("Shape of dataset:")
print(df.shape)

# يعرض اسماء الاعمده 
print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())


# ===============================
# 4. Check Missing Values
# ===============================

print("\nMissing values in each column:")
print(df.isnull().sum())


# ===============================
# 5. Data Cleaning
# ===============================

df['dep_delay'] = df['dep_delay'].fillna(0)
df['arr_delay'] = df['arr_delay'].fillna(0)


print("\nDataset shape before cleaning:")
print(df.shape)

df_clean = df.dropna(subset=['air_time'])

print("\nDataset shape after removing missing values:")
print(df_clean.shape)


# ===============================
# 6. Descriptive Statistics
# ===============================

print("\nDescriptive Statistics:")

print("\nDeparture Delay:")
print("Mean:", df_clean['dep_delay'].mean())
print("Median:", df_clean['dep_delay'].median())
print("Standard Deviation:", df_clean['dep_delay'].std())

print("\nArrival Delay:")
print("Mean:", df_clean['arr_delay'].mean())
print("Median:", df_clean['arr_delay'].median())
print("Standard Deviation:", df_clean['arr_delay'].std())

longest_flight = df_clean.loc[df_clean['distance'].idxmax()]
shortest_flight = df_clean.loc[df_clean['distance'].idxmin()]

print("\nFlight with longest distance:")
print(longest_flight)

print("\nFlight with shortest distance:")
print(shortest_flight)


# ===============================
# 7. Grouping Analysis
# ===============================

carrier_stats = df_clean.groupby('carrier')[['dep_delay', 'arr_delay']].mean()

print("\nAverage departure and arrival delay by carrier:")
print(carrier_stats)

origin_stats = df_clean.groupby('origin').agg({
    'flight': 'count',
    'distance': 'sum'
})

print("\nTotal number of flights and total distance by origin airport:")
print(origin_stats)


# ===============================
# 8. Visualization Style
# ===============================

plt.style.use('seaborn-v0_8')


# ===============================
# 9. Average Delay by Airline
# ===============================

carrier_delay = df_clean.groupby('carrier')['arr_delay'].mean()


# ===============================
# 10. Plot Average Delay by Airline
# ===============================

plt.figure(figsize=(8,5))

ax = carrier_delay.plot(kind='bar', color="#735373", edgecolor='black')

plt.title("Average Arrival Delay by Airline")
plt.xlabel("Airline Carrier")
plt.ylabel("Average Arrival Delay (minutes)")

plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(carrier_delay):
    ax.text(i, v + 0.2, round(v,2), ha='center')

plt.savefig("average_delay_by_airline.png")
plt.show()


# ===============================
# 11. Number of Flights per Month
# ===============================

flights_per_month = df_clean.groupby('month')['flight'].count()

plt.figure(figsize=(8,5))

flights_per_month.plot(kind='line', marker='o', color="#735373")

plt.title("Number of Flights per Month")
plt.xlabel("Month")
plt.ylabel("Number of Flights")

plt.grid(True)

plt.savefig("flights_per_month.png")
plt.show()


# ===============================
# 12. Departure Delay Distribution
# ===============================

plt.figure(figsize=(8,5))

plt.hist(df_clean['dep_delay'], bins=50, color="#735373", edgecolor='black', alpha=0.8)

plt.title("Distribution of Departure Delays")
plt.xlabel("Departure Delay (minutes)")
plt.ylabel("Number of Flights")

plt.savefig("departure_delay_distribution.png")
plt.show()


# ===============================
# 13. Distance vs Arrival Delay
# ===============================

plt.figure(figsize=(8,5))

plt.scatter(df_clean['distance'], df_clean['arr_delay'], color="#735373", alpha=0.4)

plt.title("Distance vs Arrival Delay")
plt.xlabel("Distance (miles)")
plt.ylabel("Arrival Delay (minutes)")

plt.savefig("distance_vs_delay.png")
plt.show()
