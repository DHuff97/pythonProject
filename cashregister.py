f = float(input("Enter price of the first item: "))

s = float(input("Enter price of the second item: "))

c = input("Does customer have a club card? (Y/N): ")

t = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
base_price = (f+s)

if f >= s:
    s = float(s * .5)
else:
    f = float(f * .5)


if c == ("Y"):
    f = float(f * .90)
    s = float(s * .90)
elif c == ("y"):
    f = float(f * .90)
    s = float(s * .90)


t = t / 100

total_price = (f+s)
d_price = (f + s) * t
discount = (d_price + total_price)
print(f"Base price = {base_price:.2f}")
print(f"Price after discounts = {total_price:.2f}")
print(f"Total price = {discount:.2f}")










