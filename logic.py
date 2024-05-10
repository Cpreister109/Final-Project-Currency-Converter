import requests

r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=a3a9da44e0e49ccb0e79dd8ed1828fa0')
currencies = r.json()
exchange_rates = currencies.get("rates", {})
exchange_rates['EUR'] = 1.00

def convert_logic(amount: int, from_curr: str, to_curr: str) -> float:

    '''
    This function contains the actual math when it comes to converting
    each currency. It utilizes an API in order to obtain the exchange
    rates in real time! Then converts the currency accordingly to the
    current options that are selected.

    :return: The finalized conversion of the specified currency
    '''

    if int(amount) < 0:

        raise TypeError

    else:

        if from_curr == 'EUR':

            from_euro = int(amount) * exchange_rates[to_curr]

            return from_euro

        elif to_curr == 'EUR':

            to_euro = int(amount) / exchange_rates[from_curr]

            return to_euro

        else:

            euros = int(amount) / exchange_rates[from_curr]
            conversion = euros * exchange_rates[to_curr]

            return conversion