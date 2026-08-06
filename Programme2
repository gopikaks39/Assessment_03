trains = [
    {
        "train_number": "12601",
        "route": "Chennai-Bengaluru",
        "total_seats": 500,
        "booked_seats": 480,
        "waiting_list": 40,
        "ticket_fare": 650,
        "cancellation_count": 20,
        "distance": 360
    },
    {
        "train_number": "12602",
        "route": "Delhi-Mumbai",
        "total_seats": 600,
        "booked_seats": 550,
        "waiting_list": 80,
        "ticket_fare": 1200,
        "cancellation_count": 30,
        "distance": 1400
    },
    {
        "train_number": "12603",
        "route": "Kochi-Trivandrum",
        "total_seats": 400,
        "booked_seats": 150,
        "waiting_list": 0,
        "ticket_fare": 250,
        "cancellation_count": 10,
        "distance": 220
    },
    {
        "train_number": "12604",
        "route": "Hyderabad-Pune",
        "total_seats": 450,
        "booked_seats": 430,
        "waiting_list": 25,
        "ticket_fare": 800,
        "cancellation_count": 15,
        "distance": 560
    },
    {
        "train_number": "12605",
        "route": "Bangalore-Mysore",
        "total_seats": 300,
        "booked_seats": 120,
        "waiting_list": 0,
        "ticket_fare": 180,
        "cancellation_count": 5,
        "distance": 145
    }
]

for train in trains:
    train["occupancy_ratio"] = train["booked_seats"] / train["total_seats"]
    actual_booked = train["booked_seats"] - train["cancellation_count"]
    train["actual_revenue"] = actual_booked * train["ticket_fare"]
    train["revenue_per_km"] = train["actual_revenue"] / train["distance"]

high_demand = [
    train for train in trains
    if train["waiting_list"] > 0 or train["booked_seats"] >= train["total_seats"]
]

max_route = max(trains, key=lambda x: x["actual_revenue"])

below_50 = [train for train in trains if train["occupancy_ratio"] < 0.5]

sorted_trains = sorted(trains, key=lambda x: x["actual_revenue"], reverse=True)

report = []
report.append("SMART RAILWAY RESERVATION REPORT\n")

for train in sorted_trains:
    report.append(
        f"{train['train_number']} | {train['route']} | "
        f"Occupancy: {train['occupancy_ratio']*100:.2f}% | "
        f"Revenue: {train['actual_revenue']:.2f} | "
        f"Revenue/KM: {train['revenue_per_km']:.2f}"
    )

report.append("\nHigh Demand Trains:")
for train in high_demand:
    report.append(f"{train['train_number']} - {train['route']}")

report.append(f"\nMaximum Revenue Route: {max_route['route']}")

report.append("\nOccupancy Below 50%:")
for train in below_50:
    report.append(f"{train['train_number']} - {train['route']}")

report.append("\nTop Three Revenue Generating Trains:")
for train in sorted_trains[:3]:
    report.append(f"{train['train_number']} - {train['route']} - {train['actual_revenue']:.2f}")

with open("railway_report.txt", "w") as file:
    file.write("\n".join(report))

with open("railway_report.txt", "r") as file:
    print(file.read())
