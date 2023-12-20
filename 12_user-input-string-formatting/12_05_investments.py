# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.



invest = float(input("Write investment amount: "))
interest_rate = float(input("Write interest rate in percentage: "))
years = int(input("Write number of years to invest: "))

for i in range(years+1):
    invest*=interest_rate

print(f"\nThis would be the future value: {invest}")