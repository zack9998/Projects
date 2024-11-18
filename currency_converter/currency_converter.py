import requests

user_currency = input("Enter you're currency please : ").lower().strip()
converted_currency = input("Enter the currency you want to convert to : ").lower().strip()
user_amount = input("input the amout please : ")

url = f"https://api.apilayer.com/currency_data/convert?to={converted_currency}&from={user_currency}&amount={user_amount}"

payload = {}
headers= {
  "apikey": "Sx8h6WcxIRUbyodsXyJ0hQAi4ndxhazi"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
results = response.json()
new_amount = results["result"]
print(f"the new amount with {converted_currency} is {new_amount}")