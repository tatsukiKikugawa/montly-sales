# reporter.py
import os
import statistics
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
print("READING GRADEBOOK CSV FILE...")
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
# # FIND AVG GRADE
# # stats["games"].max()
# grades_col = grades["final_grade"]
# print("GRADES COLUMN", type(grades_col))
# avg_grade = grades_col.mean()
# print("AVG GRADE:", avg_grade)
#
# # LOOP THROUGH ALL ROWS
#
# for index, row in grades.iterrows():
#     print(index)
#     print(row["final_grade"])
#     print("----")
# ALTERNATIVE WAY THAT MINIMIZES OUR PANDAS USAGE
print("---------------")
# convert DataFrame object to list of dictionaries:
grades_list = grades.to_dict("records")
print(type(grades_list))
print(type(grades_list[0]))
print(grades_list)
# use a list comprehension for mapping purposes:
just_grades = [float(d["final_grade"]) for d in grades_list]
print(type(just_grades))
print(just_grades[0])
print("AVG GRADE", statistics.mean(just_grades))