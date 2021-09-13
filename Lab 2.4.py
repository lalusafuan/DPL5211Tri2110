# Student ID: 1201201699
# Student Name : Lalu Muhammad Safuan Bin Maazar

PRICEB = 1.50
PRICEG = 5.60

print("Invoice for Fruits Purchase")
print("---------------------------------")

banana = int(input("Enter the quantity (comb) of bananas bought : "))
grape = float(input("Enter the amount (kg) of grapes bought : "))

totbanana = PRICEB * banana
totgrape = PRICEG * grape

print("Item \t\t\t Qty\t Price \t\t Total")
print("Banana (combs) \t\t {} \t RM{:.2f} \t RM{:.2f}".format(banana,PRICEB,totbanana))
print("Grapes (kg) \t\t {:.2f} \t RM{:.2f} \t RM{:.2f}".format(grape,PRICEG,totgrape))

total = totbanana + totgrape
print("Total: RM{:.2f}".format(total))