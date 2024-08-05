# WealthsimpletonCrypto

A Python script that scrapes your Wealthsimple crypto activity history and saves the data in a JSON file, and then converts the JSON file to CSVs that can be imported into custom wallets in Koinly for portfolio tracking / tax reporting purposes.

## Usage

1. Ensure Python dependencies are installed: `pip install -r requirements.txt`
2. Ensure you have Chromium or Google Chrome installed.
3. Ensure you have Chrome Webdriver installed and that it is compatible with the version of Chromium/Chrome you have.
   - On Linux, you can run `installChromeDriver.sh` to automatically install/update ChromeDriver in `/usr/local/bin`,
4. Run the script: `python main.py --file ws_dump.json --account_id YOUR_CRYPTO_ACCOUNT_ID`
   Replace YOUR_CRYPTO_ACCOUNT_ID with your Crypto account ID. You can find this in the URL
   when you visit wealthsimple.com and go into your Crypto account. It looks something like this:
   `non-registered-crypto-lmzx7t93`
5. Once the browser launches from the script, log into WealthSimple
6. After logging in, wait and let the `main.py` script do its thing
   Here's what `main.py` will do:
      - First, the browser will navigate to the activity page
      - Then it will click "Load more" in a loop until all transactions are loaded
      - Then it will scroll to the top
      - Then it will expand each transaction, read the details, save to memory
      - Once all transactions have been read, it will save the details to disk
7. Once the script finishes, it will write a file to disk called `ws_dump.json`
8. Run `python ws_to_koinly.py` to convert that JSON file  into a series of CSVs that can be imported into Koinly (e.g., `koinly_btc.csv`, `koinly_eth.csv`)

The Koinly CSVs are saved in a format like the "trade template" found here:
https://support.koinly.io/en/articles/9489976-how-to-create-a-custom-csv-file-with-your-data

For example...

```
Koinly Date,Pair,Side,Amount,Total,Fee Amount,Fee Currency,Order ID,Trade ID
2018-01-01 14:25 UTC,BTC-USD,Buy,1,1000,5,USD,,
2018-01-01 14:45 UTC,BTC-USD,Sell,1,900,3,USD,,
```