import csv


products = [
    {
        "Product ID": 101,
        "Product Name": "Laptop",
        "Category": "Electronics",
        "Opening Stock": 100,
        "Units Sold": 70,
        "Units Returned": 5,
        "Supplier Lead Time": 10,
        "Unit Cost": 40000,
        "Selling Price": 50000,
        "Past Demand": [60, 65, 70]
    },
    {
        "Product ID": 102,
        "Product Name": "Shoes",
        "Category": "Fashion",
        "Opening Stock": 200,
        "Units Sold": 120,
        "Units Returned": 10,
        "Supplier Lead Time": 8,
        "Unit Cost": 1000,
        "Selling Price": 1800,
        "Past Demand": [100, 110, 120]
    },
    {
        "Product ID": 103,
        "Product Name": "Rice Bag",
        "Category": "Grocery",
        "Opening Stock": 300,
        "Units Sold": 250,
        "Units Returned": 15,
        "Supplier Lead Time": 5,
        "Unit Cost": 700,
        "Selling Price": 1000,
        "Past Demand": [220, 240, 250]
    },
    {
        "Product ID": 104,
        "Product Name": "Mobile",
        "Category": "Electronics",
        "Opening Stock": 150,
        "Units Sold": 100,
        "Units Returned": 3,
        "Supplier Lead Time": 12,
        "Unit Cost": 15000,
        "Selling Price": 22000,
        "Past Demand": [90, 95, 100]
    },
    {
        "Product ID": 105,
        "Product Name": "Notebook",
        "Category": "Stationery",
        "Opening Stock": 500,
        "Units Sold": 300,
        "Units Returned": 20,
        "Supplier Lead Time": 4,
        "Unit Cost": 40,
        "Selling Price": 70,
        "Past Demand": [250, 280, 300]
    },
    {
        "Product ID": 106,
        "Product Name": "Chair",
        "Category": "Furniture",
        "Opening Stock": 80,
        "Units Sold": 60,
        "Units Returned": 2,
        "Supplier Lead Time": 15,
        "Unit Cost": 2500,
        "Selling Price": 4000,
        "Past Demand": [50, 55, 60]
    }
]


category_profit = {}

for p in products:


    p["Current Stock"] = (
        p["Opening Stock"] -
        p["Units Sold"] +
        p["Units Returned"]
    )


    p["Profit"] = (
        (p["Selling Price"] - p["Unit Cost"])
        * p["Units Sold"]
    )


    p["Reorder"] = "YES" if p["Current Stock"] < 50 else "NO"

    average_inventory = (
        p["Opening Stock"] + p["Current Stock"]
    ) / 2

    p["Inventory Turnover Ratio"] = round(
        p["Units Sold"] / average_inventory,
        2
    )

 
    p["Predicted Demand"] = round(
        sum(p["Past Demand"]) /
        len(p["Past Demand"]),
        2
    )


    category_profit[p["Category"]] = (
        category_profit.get(
            p["Category"],
            0
        ) + p["Profit"]
    )


highest = max(
    products,
    key=lambda x: x["Profit"]
)

products.sort(
    key=lambda x: x["Profit"],
    reverse=True
)

print("\nCURRENT STOCK")

for p in products:
    print(
        p["Product Name"],
        ":",
        p["Current Stock"]
    )

print("\nPROFIT")

for p in products:
    print(
        p["Product Name"],
        ":",
        p["Profit"]
    )

print("\nPRODUCTS NEEDING REORDER")

for p in products:
    if p["Reorder"] == "YES":
        print(p["Product Name"])

print("\nINVENTORY TURNOVER RATIO")

for p in products:
    print(
        p["Product Name"],
        ":",
        p["Inventory Turnover Ratio"]
    )

print("\nHIGHEST PROFIT PRODUCT")
print(
    highest["Product Name"],
    highest["Profit"]
)

print("\nCATEGORY WISE PROFIT")

for c in category_profit:
    print(
        c,
        ":",
        category_profit[c]
    )

print("\nNEXT MONTH DEMAND")

for p in products:
    print(
        p["Product Name"],
        ":",
        p["Predicted Demand"]
    )

print("\nPRODUCTS SORTED BY PROFIT")

for p in products:
    print(
        p["Product Name"],
        p["Profit"]
    )


with open(
    "inventory_report.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Product ID",
        "Product Name",
        "Category",
        "Current Stock",
        "Profit",
        "Inventory Turnover Ratio",
        "Predicted Demand"
    ])

    for p in products:
        writer.writerow([
            p["Product ID"],
            p["Product Name"],
            p["Category"],
            p["Current Stock"],
            p["Profit"],
            p["Inventory Turnover Ratio"],
            p["Predicted Demand"]
        ])

print("\nCSV FILE CREATED SUCCESSFULLY")


print("\nTOP FIVE PROFITABLE PRODUCTS")

rows = []

with open(
    "inventory_report.csv",
    "r"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        row["Profit"] = int(row["Profit"])
        rows.append(row)

rows.sort(
    key=lambda x: x["Profit"],
    reverse=True
)

for row in rows[:5]:
    print(
        row["Product Name"],
        "Profit:",
        row["Profit"]
    )
