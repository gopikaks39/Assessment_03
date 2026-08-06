portfolio = [
    {
        "investor_id": "INV101",
        "stock_symbol": "TCS",
        "quantity": 50,
        "buy_price": 3200,
        "current_price": 3600,
        "sector": "IT",
        "dividend": 5000
    },
    {
        "investor_id": "INV102",
        "stock_symbol": "INFY",
        "quantity": 80,
        "buy_price": 1500,
        "current_price": 1450,
        "sector": "IT",
        "dividend": 2000
    },
    {
        "investor_id": "INV103",
        "stock_symbol": "HDFCBANK",
        "quantity": 60,
        "buy_price": 1400,
        "current_price": 1700,
        "sector": "Banking",
        "dividend": 3000
    },
    {
        "investor_id": "INV104",
        "stock_symbol": "RELIANCE",
        "quantity": 40,
        "buy_price": 2400,
        "current_price": 2800,
        "sector": "Energy",
        "dividend": 4000
    },
    {
        "investor_id": "INV105",
        "stock_symbol": "WIPRO",
        "quantity": 100,
        "buy_price": 500,
        "current_price": 470,
        "sector": "IT",
        "dividend": 1500
    }
]

sector_exposure = {}
investors = {}

for stock in portfolio:
    stock["investment_value"] = stock["quantity"] * stock["buy_price"]
    stock["current_value"] = stock["quantity"] * stock["current_price"] + stock["dividend"]
    stock["profit_loss"] = stock["current_value"] - stock["investment_value"]
    stock["percentage_return"] = (stock["profit_loss"] / stock["investment_value"]) * 100

    sector_exposure[stock["sector"]] = sector_exposure.get(stock["sector"], 0) + stock["current_value"]

    investors[stock["investor_id"]] = investors.get(stock["investor_id"], 0) + stock["percentage_return"]

best_stock = max(portfolio, key=lambda x: x["percentage_return"])
worst_stock = min(portfolio, key=lambda x: x["percentage_return"])

ranked_investors = sorted(investors.items(), key=lambda x: x[1], reverse=True)

report = []
report.append("SMART STOCK PORTFOLIO REPORT\n")

for stock in portfolio:
    report.append(
        f"{stock['investor_id']} | {stock['stock_symbol']} | "
        f"Investment: {stock['investment_value']:.2f} | "
        f"Current: {stock['current_value']:.2f} | "
        f"Profit/Loss: {stock['profit_loss']:.2f} | "
        f"Return: {stock['percentage_return']:.2f}%"
    )

report.append(f"\nBest Performing Stock: {best_stock['stock_symbol']}")
report.append(f"Worst Performing Stock: {worst_stock['stock_symbol']}")

report.append("\nSector Wise Exposure:")
for sector, value in sector_exposure.items():
    report.append(f"{sector}: {value:.2f}")

report.append("\nInvestor Ranking:")
for investor, value in ranked_investors:
    report.append(f"{investor}: {value:.2f}%")

with open("portfolio_report.txt", "w") as file:
    file.write("\n".join(report))

with open("portfolio_report.txt", "r") as file:
    print(file.read())
