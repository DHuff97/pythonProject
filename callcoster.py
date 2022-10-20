d = input("Enter the day the call started at: ")

t = int(input("Enter the time the call started at (hhmm): "))

m = int(input("Enter the duration of the call (in minutes): "))

weekdays = ["Mon", "Tue", "Wed", "Thr", "Fri"]

weekend = ["Sat", "Sun"]


if d in weekend:
    cost = m * .15
elif d in weekdays and 800 <= t <= 1800:
    cost = m * .40
else:
    cost = m * .25

print(f"This call will cost ${cost:.2f}")

