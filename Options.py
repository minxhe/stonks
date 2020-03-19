import pandas as pd
import sys
from wallstreet import Call, Put

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
    options.append([price, option.price, option.implied_volatility(), option.volume, option.underlying.price, option.delta(), option.gamma(), option.theta(), option.expiration])

    price += step

df = pd.DataFrame(options, columns = ['Strike', 'Price', 'Implied Vol', 'Volume', 'Underlying', 'Delta', 'Gamma', 'Theta', 'Expiration'])
print(df)