import sys
import requests

def prg_exit(err_msg):
    print(err_msg)
    sys.exit(1)

def get_bitcoin():
    try:
        bitcoin_information_request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_json = bitcoin_information_request.json()
        bitcoin = bitcoin_json['bpi']['USD']['rate_float']
        dollars_bitcoin = bitcoin * amount
        print(f"${dollars_bitcoin:,.4f}")
    except requests.RequestException:
         prg_exit("Bitcoin information not available")

if len(sys.argv) == 2:
    try:
         amount = float(sys.argv[1])
         get_bitcoin()

    except:
        prg_exit("Command-line argument is not a number")
else:
     prg_exit("Missing command-line argument")