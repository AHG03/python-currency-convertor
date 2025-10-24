currencies = ("eur", "usd", "cad")

exchange_rates = {
    "usd": {"eur":0.85 , "cad":1.25 },
    "eur": {"usd":1.18 , "cad":1.47 },
    "cad": {"usd":0.80 , "cad":0.68 },
}

while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Invalid input")

while True:
    source_currency = input("Source currency (USD/EUR/CAD): ").lower()
    if source_currency not in currencies:
        print("Invalid input")
    else:
        break

while True:
    target_currency = input("Target currency (USD/EUR/CAD): ").lower()
    if target_currency not in currencies:
        print("Invalid input")
    else:
        break

if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * exchange_rates[source_currency][target_currency]
    print(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}.")