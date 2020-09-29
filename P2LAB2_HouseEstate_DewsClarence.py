current_price = int(input())
last_months_price = int(input())

monthly_mortgage = (current_price * 0.051) / 12

print("This house is ${}. The change is ${} since last month.".format(current_price, current_price - last_months_price))
print("The estimated monthly mortgage is ${:.2f}.".format(monthly_mortgage))
   