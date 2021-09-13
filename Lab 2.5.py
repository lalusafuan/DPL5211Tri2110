# Student ID: 1201201699
# Student Name : Lalu Muhammad Safuan Bin Maazar

litres = total = 0.0

PRICE = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

litres = float(input("Enter amount of litres : "))

print("Price per litre = RM {:.2f}".format(PRICE))
print("Number of liters = {}".format(litres))

total = litres * PRICE

print("Total : RM {:.2f}".format(total))
