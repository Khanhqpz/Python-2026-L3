a = int(input("Enter a perfect numbner: "))
sum_divisors = 0

for i in range(1, a):
    if a % i == 0: 
        sum_divisors += i
if sum_divisors == a and sum_divisors >1:
    print(a, "is a perfect number")
else:
    print(a, "is not a perfect number")
