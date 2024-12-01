import pandas as pd

# Load the dataset
df = pd.read_csv('retail_sales_dataset.csv')

# Show the first 5 rows of the data to check if it's loaded correctly
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Drop duplicate rows if any
df = df.drop_duplicates()

# Remove rows where Sales are negative (just in case)
df = df[df['Total Amount'] >= 0]

# 1.Calculate total sales
total_sales = df['Total Amount'].sum()
print(f"Total Sales: {total_sales}")

# 2.Group sales by gender
sales_per_gender = df.groupby('Gender')['Total Amount'].sum()

# Print the sales by Gender
print(sales_per_gender)

# 3.Group sales by product category
sales_by_product_category = df.groupby('Product Category')['Total Amount'].sum()

# Print the sales by product category
print(sales_by_product_category)


# 4. Visualize the Data
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize sales by gender
plt.figure(figsize=(8, 6))
sns.barplot(x=sales_per_gender.index, y=sales_per_gender.values, palette='viridis')
plt.title('Sales by gender')
plt.xlabel('gender')
plt.ylabel('TotalAmount')
plt.show()


# 5.Sales Trend Over Time

# Create a new column for the month
df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')

# Group sales by month
sales_per_month = df.groupby('Month')['Total Amount'].sum()

# Plot sales over time
plt.figure(figsize=(10, 6))
sales_per_month.plot(kind='line', color='purple')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.show()


#6.  Generate Insights

# Insight 1: Highest Sales Gender
highest_sales_region = sales_per_gender.idxmax()
print(f"Gender with the highest sales: {highest_sales_region}")

# Insight 2: Best Selling Category
best_selling_category = sales_by_product_category .idxmax()
print(f"Best Selling Category: {best_selling_category}")
