# Final Assignment

## System
1. MacOS 12.3.1
2. MySQL Workbench 8.0.31 Community
3. PyCharm 2023.1 (Community Edition)
4. Python 3.11 Interpreter
5. Tableau Public 2023.1.0

---

## Step 1, sql

- Execute the provided [finance_liquor_sales.sql](https://github.com/Workearly/Final-Assignment/blob/main/finance_liquor_sales.sql) in MySQL Workbench to create the necesseary schema.
- Execute the [sql_query.sql](https://github.com/fdiamant/workearly_final_assignment/blob/main/sql_query.sql) to retrieve all columns between 2016 and 2019
- Export the results in a csv file. [liquor_sales.csv](https://github.com/fdiamant/workearly_final_assignment/blob/main/liquor_sales.csv)

## Step 2, python

### Missing values handling

After calculating the percentage of missing values per column, it becomes evident that a significant portion of the missing value data is observed in the store_location column (12.16%) and the category_name column (8.11%). However, as the significant columns here are not category_name and store_location, it is not necessary to drop the indexes with missing values.

See the [liquor_sale.py](https://github.com/fdiamant/workearly_final_assignment/blob/main/liquor_sales.py) for details.