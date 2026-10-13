a = int(input("Enter prime number: "))

Prime = True

if a <=1:
    Prime = False
else:
    for i in range(2,a):
        if a % i == 0:
          Prime = False
        break
if Prime:
  print(a, "is not a prime number")
else:
  print(a, "is a prime number") 
