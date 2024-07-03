import pandas as pd

# Load the dataset (assuming it's named "Automobile_data.csv")
df = pd.read_csv("Automobile_data.csv")

# 1. First and Last Five Rows
print("First five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

# 2. Toyota Cars Details
toyota_cars = df[df["company"] == "Toyota"]
print("\nDetails of Toyota cars:")
print(toyota_cars)

# 3. Total Cars per Company
car_counts = df["company"].value_counts()
print("\nTotal cars per company:")
print(car_counts)

# 4. Highest Price Car per Company
max_prices = df.groupby("company")["price"].max()
print("\nHighest price car per company:")
print(max_prices)

# 5. Average Mileage by Car Making Company
avg_mileage = df.groupby("company")["mileage"].mean()
print("\nAverage mileage by company:")
print(avg_mileage)

# 6. Sort all cars by Price
sorted_df = df.sort_values(by="price")
print("\nCars sorted by price:")
print(sorted_df)

# 7. Check for Null Values
null_values = df.isnull().sum()
print("\nNull values in the dataset:")
print(null_values)
