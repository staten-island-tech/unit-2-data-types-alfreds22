def find_factors(num):
    if num <= 0:
        return "Please enter a positive integer."
    factors = []  
    for i in range(1, num + 1):
        if num % i == 0: 
            factors.append(i)  
    return f"Factors of {num}: {factors}" 
number = input("Enter a positive integer: ")
if number.isdigit():  
    number = int(number)  
    print(find_factors(number))  
else:
    print("Please enter a valid positive integer.")

    

