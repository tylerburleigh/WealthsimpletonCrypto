import json
import csv
from datetime import datetime
from collections import defaultdict

# Read the JSON data
with open('ws_dump.json', 'r') as file:
    data = json.load(file)

# Create a dictionary to store transactions for each cryptocurrency
crypto_transactions = defaultdict(list)

# Process each transaction
for transaction in data:
    # Parse the date
    date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S")
    koinly_date = date.strftime("%Y-%m-%d %H:%M UTC")
    
    # Determine the pair and side
    crypto = transaction['description']
    pair = f"{crypto}-CAD"
    side = "Buy" if transaction['type'] == "Market buy" else "Sell"
    
    # Extract the amount and total
    amount = transaction['filled_quantity'].split()[0]
    total = transaction['amount'].replace("$", "").replace(" CAD", "")
    
    # Extract the fee
    fee_amount = transaction['fees'].replace("$", "").replace(" CAD", "")
    fee_currency = "CAD"
    
    # Create a row for this transaction
    row = [koinly_date, pair, side, amount, total, fee_amount, fee_currency, "", ""]
    
    # Add this row to the appropriate cryptocurrency list
    crypto_transactions[crypto].append(row)

# Write a CSV file for each cryptocurrency
for crypto, transactions in crypto_transactions.items():
    filename = f"koinly_{crypto.lower()}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Write the header
        writer.writerow(["Koinly Date", "Pair", "Side", "Amount", "Total", "Fee Amount", "Fee Currency", "Order ID", "Trade ID"])
        
        # Write all transactions for this cryptocurrency
        writer.writerows(transactions)
    
    print(f"Created {filename} with {len(transactions)} transactions.")