n = int(input("Please enter a positive integer greater than 1: "))
prior_sum = 0
current_sum = 1
count = 0
while count < n:
    print(current_sum)
    new = current_sum + prior_sum
    prior_sum = current_sum
    current_sum = new
    count += 1





