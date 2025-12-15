# pcost.py
#
# Exercise 1.27
# Exercise 1.30 - 1.33

import sys

def portfolio_cost(filename):
    'Calculates the total cost of the portfolio added as an input file'
    total_cost = 0.0
    with open(filename) as file:
        headers = next(file)
        for line in file:
            data = line.split(',')
            try:
                shares = int(data[1])
            except ValueError:
                print("Couldn't parse", line)

            try:
                price = float(data[2])
            except ValueError:
                print("Couldn't parse", line)
            
            total_cost += shares * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)