# reporter.py
import pandas
import os
import csv
import statistics
import datetime

def to_usd(my_price):
  return f"${my_price:,.2f}"

if __name__ == "__main__":
    print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")

    sales_filepath = os.path.join(os.path.dirname(__file__), "data", "sales-201903.csv")

# IMPORT CSV
    rows = []
    with open(sales_filepath,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for r in reader:
            rows.append(dict(r))
    
    sales_price = [float(row["sales price"]) for row in rows]

    total_sales = sum(sales_price)

    months = [
    {"id":"01", "month": "January"},
    {"id":"02", "month": "February"},
    {"id":"03", "month": "March"},
    {"id":"04", "month": "April"},
    {"id":"05", "month": "May"},
    {"id":"06", "month": "June"},
    {"id":"07", "month": "July"},
    {"id":"08", "month": "August"},
    {"id":"09", "month": "September"},
    {"id":"10", "month": "October"},
    {"id":"11", "month": "November"},
    {"id":"12", "month": "December"}
    ]
    
    year = sales_filepath[11:-6]
    month = sales_filepath[15:-4]
    
    month_name = [m for m in months if m["id"] == month]
    name = month_name[0]

    
    print("-------------------------")
    print("SALES REPORT (" + name["month"] + " " + year + ")")
    print("-------------------------")
    print("TOTAL SALES: " + str(to_usd(total_sales)))
    print("-------------------------")


 



   



