color_list = ["Blue", "Red", "Yellow", "Grey"]
user_color = input("What is your favorite color? ")
if user_color in color_list:
    idx = color_list.index(user_color)
    print("the index of this color in the list.")
else:
       print("Sorry, I could not find your color")
