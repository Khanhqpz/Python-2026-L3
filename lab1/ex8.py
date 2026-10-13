I = [1, 4, 5, -1, 10]

def extracted_even(I):
    result = []
    for i in I:
        if i % 2 ==0:
            result.append(i)
    return result
print("A list:", extracted_even(I)) 
    

    
    