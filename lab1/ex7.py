def remove_dollar_sign(s):
    return s.replace("$", "")

s = input("How much?  ")
print("Price: ", remove_dollar_sign(s))
    

