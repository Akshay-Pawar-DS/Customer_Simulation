import csv
import datetime
import random

#function to generate random date
def random_date(start, end):
  return start + datetime.timedelta(
      seconds=random.randint(0, int((end - start).total_seconds())))

start = datetime.date(2023, 4, 1)
end = datetime.date(2023, 10, 18) 


field_names = ["CustomerID", "VisitDate", "TotalSpend", "ProductCategory"]


with open('data.csv', 'w', newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()

    for customer_id in range(1, 501):  # Generating 500 records
        visit_date = random_date(start, end)
        total_spend = round(random.uniform(10, 2000), 2)  # Random total spend between 10 and 2000
        product_category = random.choice(["Fashion","Electronics","Grocery","Furniture","Books", "Home", "Sports"])

        writer.writerow({
            "CustomerID": customer_id,
            "VisitDate": visit_date,
            "TotalSpend": total_spend,
            "ProductCategory": product_category
        })