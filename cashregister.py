f = float(input("Enter price of the first item: "))

s = float(input("Enter price of the second item: "))

c = input("Does customer have a club card ?(Y/N): ")

t = float(input("Enter tax rate, e.g 5.5 for 5.5% tax: "))
base_price = (f+s)

if f >= s:
    s = float(s * .5)
    s = round(s, 2)
    f = round(f, 2)

else:
    f = float(f * .5)
    s = round(s, 2)
    f = round(f, 2)

if c == ("Y"):
    f = float(f * .90)
    s = float(s * .90)
    s = round(s, 2)
    f = round(f, 2)

elif c == ("y"):
    f = float(f * .90)
    s = float(s * .90)
    s = round(s, 2)
    f = round(f, 2)

t = t / 100
price1 = (t*f)
price = (t*s)
total_price = (f+s+price+price1)
total_price = round(total_price, 2)
d_price = (f + s)
print(f"Base price = {base_price:.2f}")
print(f"Price after discounts = {d_price:.2f}")
print(f"Total price = {total_price:.2f}")










