exchange_rates = {
    'USD': 1.00,
    'EUR': 0.91,
    'CNY': 7.22,
    'JPY': 144.68,
    'TRY': 27.03,
    'MXN': 17.00,
    'BRL': 4.87,
    'INR': 82.62,
    'CAD': 1.34,
    'COP': 3955.00}


def convert_currency(amount, from_currency, to_currencies):
    """
    Converts an amount from one currency to multiple target currencies.

    :param amount: The amount in the 'from_currency'.
    :param from_currency: The source currency code.
    :param to_currencies: A list of target currency codes.
    :return: A dictionary containing converted amounts for each target currency.
    """

    if from_currency not in exchange_rates or any(currency not in exchange_rates for currency in to_currencies):
        return {"error": "Currency not supported or invalid."}

    amount_usd = amount / exchange_rates[from_currency]

    converted_amounts = {}
    for to_currency in to_currencies:
        converted_amount_per_currency = amount_usd * exchange_rates[to_currency]
        converted_amounts[to_currency] = converted_amount_per_currency

    return converted_amounts


# Get user input
amount_to_convert = float(input("Enter the amount to convert: "))
source_currency = (input("Enter the source currency code: ")).upper()
target_currencies = (input("Enter target currency codes (comma-separated): ")).upper().split(',')

converted_amounts_result = convert_currency(amount_to_convert, source_currency, target_currencies)

if "error" in converted_amounts_result:
    print(converted_amounts_result["error"])
else:
    for target_currency, converted_amount_result in converted_amounts_result.items():
        print(f"{amount_to_convert} {source_currency} is equal to {converted_amount_result:.2f} {target_currency}.")
