import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set this option to display all columns in PyCharm console
# See https://pandas.pydata.org/docs/user_guide/options.html
# display.width : int
#     Width of the display in characters. In case python/IPython is running in
#     a terminal this can be set to None and pandas will correctly auto-detect
#     the width.
pd.options.display.width = 0

# Import the data
df = pd.read_csv('liquor_sales.csv')

# Check for missing values
missing = df[df.isna().any(axis=1)]
# calculate percentage of missing values per column
missing_percentages = round((df.isna().mean() * 100), 2)
# Print the results
# print('Rows with missing or null values:\n', missing)
# print('Percentage of missing values per column:\n', missing_percentages)
# After calculating the percentage of missing values per column, it becomes evident that a significant portion of the
# missing value data is observed in the store_location column (12.16%) and the category_name column (8.11%). However,
# as the significant columns here are not category_name and store_location, it is not necessary to drop the indexes
# with missing values.

# Aggregate by zip code and item description and calculate the total number of bottles sold.
popular_items = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum()
# Sort by zip code and item description
popular_items = popular_items.sort_index(level=['zip_code', 'item_description'])

# Aggregate by store number and name. Calculate the total sales per store in dollars.
sales_per_store = df.groupby(['store_number', 'store_name'])['sale_dollars'].sum()
# Calculate the total sales in dollars.
total_sales = df['sale_dollars'].sum()
# Calculate the sales percentage per store and sort by descending value.
sales_percentage = round(100 * sales_per_store / total_sales, 2)
sales_percentage = sales_percentage.sort_values(ascending=False)
# Print the results
print('The most popular items per zip code are:\n', popular_items)
print('The sales per store are:\n', sales_percentage)

# Create the scatter plot

# Define the x and y variables
x = popular_items.index.get_level_values('zip_code')
y = popular_items.values

# Define the colors for each item description
unique_items = df['item_description'].unique()
colors = plt.cm.gnuplot2(np.linspace(0, 1, len(unique_items)))
colormap = dict(zip(unique_items, colors))

# Create the scatter plot
plt.scatter(x, y, c=[colormap[item] for item in popular_items.index.get_level_values('item_description')])

# Add labels and title
plt.xlabel('Zip Code')
plt.ylabel('Total Bottles Sold')
plt.title('Most Popular Items by Zip Code')

# Show the plot
plt.show()
