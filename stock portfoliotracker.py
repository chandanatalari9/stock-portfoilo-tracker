# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment_value = price * quantity

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "value": investment_value
        })

        total_investment += investment_value

        print(
            f"{stock_name}: {quantity} shares × "
            f"${price} = ${investment_value}"
        )

    except ValueError:
        print("Please enter a valid number for quantity.")

print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

if portfolio:
    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: ${item['price']} | "
            f"Value: ${item['value']}"
        )

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total_investment}")
else:
    print("No stocks were added.")

# Save results to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 40 + "\n\n")

    for item in portfolio:
        file.write(
            f"Stock: {item['stock']}\n"
            f"Quantity: {item['quantity']}\n"
            f"Price: ${item['price']}\n"
            f"Investment Value: ${item['value']}\n"
            f"-" * 30 + "\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}\n")

print("\nPortfolio saved successfully to portfolio_summary.txt")