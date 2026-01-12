# report.py
#
# Exercise 2.4
# Exercise 2.5
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # Exercise 2.4 assign as tuple
            # holding = (row[0], int(row[1]), float(row[2])) 
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio

# Exercise 2.6
def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    stock_prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                    pass
     
    return stock_prices

# Exercise 2.7
portfolio_filename = './Data/portfolio.csv'
prices_filename = './Data/prices.csv'

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)

original_value = 0.0
current_value = 0.0
for s in portfolio:
     original_value += s['shares']*s['price']
     if s['name'] in prices:
          current_value += s['shares']*prices[s['name']] 
     else:
          print(s,'not in price list')

print('Current portfolio value = ', current_value)
if current_value - original_value >= 0.0:
     print('Gain = %.2f' %(current_value - original_value))
else:
     print("Loss = %.2f" %(current_value - original_value))
