# reporter.py

import os
import pandas

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")

print("READING GRADEBOOK CSV FILES....")

# if CSV file in same dir as this Python script:
# csv_filepath = "gradebook2.csv"
# if CSV file in the data dir:
# csv_filepath = "data/gradebook.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "gradebook.csv")
print("FILEPATH:", os.path.abspath(csv_filepath))
grades = pandas.read_csv(csv_filepath)
print("GRADES:", type(grades))

#print(dir(grades))

print(grades.tail())

# grades["student_id"]
# grades["final_grade"]


# FIND AVG GRADE
# stats["games"].max()
grades_col = grades["final_grade"]
print("GRADES COLUMN", type(grades_col))
avg_grade = grades_col.mean()
print("AVG GRADE:", avg_grade)
# LOOP THROUGH ALL ROWS
# use for loop


#Looping through all rows.
#my_grades = []

for index, row in grades.iterrows():
    print(index)
    print(row["final_grade"])
    print("-----")
    #my_grades.append(row["final_grade"])

#====================================
#csv_filepath = "            "
#stats = pandas.read_csv(csv_filepath)
#
##if csv files in the same dir as this python script
#csv_filepath = "monthly-sales-data/gradebook2.csv"
#grades = pandas.read_csv(csv_filepath)
#print("GRADES:", type(grades))
#print(dir(grades))
#
#print(grades.tail())
#
#
#
##from os module; s.path.join(os.path.dirname(__file__), "../data/monthly_sales.csv")