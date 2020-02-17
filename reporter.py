# reporterp.py
#No pandas version
import os
import csv
import itertools
from operator import itemgetter

def to_usd(my_price):
    # return "${0:,.2f}".format(my_price)
    return f"${my_price:,.2f}" #> $12,000.71

#
#INFO INPUTS
#

CSV_FILENAME = "sales-201803.csv"
#construct the path to a specific csv data here.
csv_filepath = os.path.join("monthly-sales-data", CSV_FILENAME)

rows = []
#Reading csv files: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/csv.md
with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od))

#print(rows[0]) #>{'date': '2018-03-01', 'product': 'Button-Down Shirt', 'unit price': '65.05', 'units sold': '2', 'sales price': '130.10'}
#float_value = float(rows[0]["sales price"])
#print(float_value) #>130.1

#list comprehensino for mapping!
sales_prices = [float(row["sales price"]) for row in rows]
total_sales = sum(sales_prices)

#Further challenge codes here:
product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"]) for row in product_rows])
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:3]

month = "March"
year = 2018

#
#INFO OUTPUTS
#

print("-------------------------")
print(f"SALES REPORT! (MONTH: {month} {year})")
print(f"TOTAL SALES: {to_usd(total_sales)}")
print("-------------------------")
print("TOP SELLING PRODUCTS: ")

counter = 0
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    print(f" {counter}. {product_name} ({sales_usd})")