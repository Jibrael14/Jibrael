from colorama import Fore, Style, init
init(autoreset=True)

rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'PKR': 277.5,
    'INR': 83.2
}

# Header
print(Fore.CYAN + "="*45)
print(Fore.YELLOW + "         🧮 Currency Converter")
print(Fore.CYAN + "="*45)
print(Fore.GREEN + "Available Currencies: USD, EUR, PKR, INR\n")

try:
    # Inputs
    amount = float(input(Fore.LIGHTWHITE_EX + "Enter amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    print(Fore.BLUE + "\nConverting...\n")


    if from_currency in rates and to_currency in rates:
        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]

        print(Fore.MAGENTA + "-"*45)
        print(Fore.LIGHTGREEN_EX + f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
        print(Fore.MAGENTA + "-"*45)
        print(Fore.BLUE + "\nConverted\n")
    else:
        print(Fore.RED + "❌ Invalid currency code. Use: USD, EUR, PKR, INR")

except ValueError:
    print(Fore.RED + "❌ Please enter a valid number.")
