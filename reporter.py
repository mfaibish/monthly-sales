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

    sales_filepath = os.path.join(os.path.dirname(__file__), "data", "sales-201902.csv")

# IMPORT CSV
    rows = []
    with open(sales_filepath,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for r in reader:
            rows.append(dict(r))
    
    sales_price = [float(row["sales price"]) for row in rows]

    total_sales = sum(sales_price)
    print(to_usd(total_sales))

    

   



