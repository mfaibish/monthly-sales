# reporter.py
import pandas
import os

if __name__ == "__main__":
   print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")

   sales_filepath = os.path.join(os.path.dirname(__file__), "data", "sales-201902.csv")

   df = pandas.read_csv(sales_filepath)

   print(df)
   



