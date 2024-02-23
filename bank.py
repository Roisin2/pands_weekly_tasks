# read in the amounts in cents
amount1 = 65
amount2 = 180

# change to Euro (100c in a euro)
e1 = amount1 / 100
e2 = amount2 / 100

# add the two amounts
total_money = e1 + e2

# print the amounts with decimal point and only two numbers after the point. 
print (f"the sum of the amounts is €{total_money:.2f}")

# referrence https://pythonguides.com/python-print-2-decimal-places/