import pandas as pd
import sys
from wallstreet import Call, Put

def format(number):
    return f'{number:10.4f}'

args = sys.argv

method = args[1]
symbol = args[2]
day = int(args[3])
month = int(args[4])
year = int(args[5])
min_strike = int(args[6])
max_strike = int(args[7])
step = int(args[8])

options = []
price = min_strike

while price <= max_strike:
    option = Call(symbol, d=day, m=month, y=year, strike=price) if method == 'call' else Put(symbol, d=day, m=month, y=year, strike=price)
    options.append([option.strike, option.price, option.underlying.price, format(option.implied_volatility()), format(option.delta()), format(option.gamma()), format(option.theta()), option.expiration])

    price += step

df = pd.DataFrame(options, columns = ['Strike', 'Price', 'Underlying', 'Implied Vol', 'Delta', 'Gamma', 'Theta', 'Expiration'])
print(df)