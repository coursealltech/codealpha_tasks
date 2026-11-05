# Stock Portfolio Tracker - CodeAlpha Python Internship (Task 2)

# fixed prices of the stocks (in dollars)
prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330, "AMZN": 130}

# this will store the stock name and how many the user bought
portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print()
print("Available stocks:")
for name in prices:
    print(name, "- $" + str(prices[name]))

# keep asking until the user types done
while True:
    print()
    stock = input("Enter stock name (or type done to finish): ")
    stock = stock.upper().strip()

    if stock == "DONE":
        break

    # check if the stock is in our price list
    if stock not in prices:
        print("Sorry, that stock is not available.")
        continue

    # ask for quantity, it must be a whole number
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if quantity <= 0:
        print("Quantity must be at least 1.")
        continue

    # if the stock was already added, add to the old quantity
    if stock in portfolio:
        portfolio[stock] = portfolio[stock] + quantity
    else:
        portfolio[stock] = quantity

    print("Added", quantity, "of", stock)

# show the result
print()
if len(portfolio) == 0:
    print("You did not add any stocks.")
else:
    total = 0
    lines = []

    print("----- Your Portfolio -----")
    for stock in portfolio:
        quantity = portfolio[stock]
        price = prices[stock]
        value = price * quantity
        total = total + value

        line = stock + ": " + str(quantity) + " x $" + str(price) + " = $" + str(value)
        print(line)
        lines.append(line)

    print("--------------------------")
    print("Total investment: $" + str(total))

    # save the result in a text file
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        for line in lines:
            file.write(line + "\n")
        file.write("Total investment: $" + str(total) + "\n")

    print()
    print("Result saved in portfolio.txt")