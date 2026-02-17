def currency_converter():
    # Mapping codes to exchange rates (1 Unit to INR)
    exchange_rates = {
        "USD": 90.72,  "EUR": 110.39, "GBP": 126.80, 
        "JPY": 0.60,   "AUD": 64.28
    }

    # Mapping codes to their currency symbols
    symbols = {
        "USD": "$", "EUR": "€", "GBP": "£", 
        "JPY": "¥", "AUD": "A$", "INR": "₹"
    }

    print("--- Multi-Currency to INR Converter ---")
    print(f"Available Currencies: {', '.join(exchange_rates.keys())}")
    
    currency = input("Enter the currency code (e.g., USD): ").upper()
    
    if currency in exchange_rates:
        try:
            amount = float(input(f"Enter the amount in {currency}: "))
            
            if amount < 0:
                print("Amount cannot be negative.")
                return

            # Conversion calculation
            inr_value = amount * exchange_rates[currency]
            
            # Using symbols in the output
            input_sym = symbols.get(currency, "")
            inr_sym = symbols["INR"]

            print("-" * 35)
            print(f"{input_sym}{amount:,} {currency} = {inr_sym}{inr_value:,.2f} INR")
            print("-" * 35)
            
        except ValueError:
            print("Error: Please enter a valid numeric number.")
    else:
        print(f"Error: '{currency}' is not in our database.")

if __name__ == "__main__":
    currency_converter()