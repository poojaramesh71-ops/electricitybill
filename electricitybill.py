def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 4)
    else:
        bill = (100 * 2) + (100 * 4) + ((units - 200) * 6)

    return bill


units = int(input("Enter number of units consumed: "))

total_bill = calculate_electricity_bill(units)
print("Total Electricity Bill: ₹",total_bill)
