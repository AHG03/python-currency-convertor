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

def convert(amount, source_currency, target_currency):
    exchange_rates = {
        "usd": {"eur": 0.85, "cad": 1.25},
        "eur": {"usd": 1.18, "cad": 1.47},
        "cad": {"usd": 0.80, "eur": 0.68},
    }

    if source_currency == target_currency:
        return amount
    return amount * exchange_rates[source_currency][target_currency]

amount = get_amount()
source_currency = get_currency("Source")
target_currency = get_currency("Target")
print(f"{amount} {source_currency} is equal to {target_currency}.")