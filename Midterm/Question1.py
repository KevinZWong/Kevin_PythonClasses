TIME_PERIOD = 1

Balance  = int(input("Input Balance: "))
Interest_Rate = float(input("Input Interest Rate: "))

monthly_interest = Balance * (1 + (Interest_Rate / 100) * TIME_PERIOD) - Balance

print("Next month interest = $", monthly_interest)
