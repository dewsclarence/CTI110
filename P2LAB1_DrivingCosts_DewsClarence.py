miles = float(input())
cost_per_gallon = float(input())

miles20 = 20 * (1.0 / miles) * cost_per_gallon
miles75 = 75 * (1.0 / miles) * cost_per_gallon
miles500 = 500 * (1.0 / miles) * cost_per_gallon

print('{:.2f} {:.2f} {:.2f}'.format(miles20, miles75, miles500))
