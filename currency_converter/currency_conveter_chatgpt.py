import requests


# Define your API key

API_KEY = "Sx8h6WcxIRUbyodsXyJ0hQAi4ndxhazi"


# Function to fetch and display all available currencies

def display_available_currencies():
    jls_extract_var = "https://api.openweathermap.org/data/3.0/onecall/day_summary?date={2024-11-05}&appid={API key}"
    url = jls_extract_var  # Replace with the actual endpoint for fetching currencies

    headers = {"apikey": API_KEY}


    response = requests.get(url, headers=headers)
    return



# Function to validate currency format

def is_valid_currency(currency):

    return len(currency) == 3 and currency.isalpha()


# Function to validate amount input

def is_valid_amount(amount):

    try:

        float(amount)

        return True

    except ValueError:

        return False


# Display all available currencies before asking for input

display_available_currencies()


# Prompt the user for currency and amount inputs

user_currency = input("Enter your currency (3-letter code, e.g., USD): ").lower().strip()

if not is_valid_currency(user_currency):

    print("Invalid currency format. Please enter a 3-letter currency code.")

else:

    converted_currency = input("Enter the currency you want to convert to (3-letter code, e.g., EUR): ").lower().strip()

    if not is_valid_currency(converted_currency):

        print("Invalid currency format. Please enter a 3-letter currency code.")

    else:

        user_amount = input("Input the amount you want to convert: ")

        if not is_valid_amount(user_amount):

            print("Invalid amount. Please enter a numeric value.")

        else:

            url = f"https://api.apilayer.com/currency_data/convert?to={converted_currency}&from={user_currency}&amount={user_amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)


            if response.status_code == 200:

                results = response.json()

                new_amount = results["result"]

                print(f"The converted amount is: {new_amount}")

            else:

                print("Error:", response.status_code, response.text)

