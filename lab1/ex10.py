def get_divisors(num):
    result = []
    for i in range(1, num + 1):
        if num % i ==0:
            result.append(i)
    return result
a = int(input("Enter:"))
print("RS", get_divisors(a))
    