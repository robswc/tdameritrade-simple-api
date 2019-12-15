import requests

key = 'YOUR API KEY HERE'

def get_quotes(**kwargs):

    # Define endpoint URL
    url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

    # Create parameters, update api key.
    params = {}
    params.update({'apikey': key})

    # Create and fill the symbol_list list with symbols from argument
    symbol_list = [symbol for symbol in kwargs.get('symbol')]
    params.update({'symbol': symbol_list})

    # Create request, with URL and parameters
    return requests.get(url, params=params).json()

def get_ohlc(**kwargs):
    data = get_quotes(symbol=kwargs.get('symbol'))
    for symbol in kwargs.get('symbol'):
        print(symbol)
        print(data[symbol]['lastPrice'])



get_ohlc(symbol=['AAPL', 'AMD', 'TSLA'])