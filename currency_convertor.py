def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid input")

def get_currency(label):
    currencies = ("eur", "usd", "cad")
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD): ").lower()
        if currency not in currencies:
            print("Invalid input")
        else:
            return currency

amount = get_amount()
source_currency = get_currency("Source")
target_currency = get_currency("Target")

exchange_rates = {
    "usd": {"eur":0.85 , "cad":1.25 },
    "eur": {"usd":1.18 , "cad":1.47 },
    "cad": {"usd":0.80 , "eur":0.68 },
}

if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * exchange_rates[source_currency][target_currency]
    print(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}.")