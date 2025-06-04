import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "rates" not in data:
        print("Error fetching exchange rates.")
        return None

    rates = data["rates"]
    if target_currency.upper() not in rates:
        print(f"Currency '{target_currency}' not found.")
        return None

    return rates[target_currency.upper()]

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        return None
    converted_amount = amount * rate
    return converted_amount

# --- Main Program ---
print("=== Currency Converter ===")
base = input("Enter base currency (e.g., USD): ").strip()
target = input("Enter target currency (e.g., INR): ").strip()
try:
    amt = float(input("Enter amount to convert: "))
    result = convert_currency(amt, base, target)
    if result is not None:
        print(f"{amt:.2f} {base.upper()} = {result:.2f} {target.upper()}")
except ValueError:
    print("Please enter a valid number.")
