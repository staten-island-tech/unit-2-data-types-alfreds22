def find_gcf(num1, num2):
    if num1 < 0 or num2 < 0:
        return "Both numbers should be non-negative."
    smaller = num1 if num1 < num2 else num2
    gcf = 1 
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i 
    return gcf
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = find_gcf(num1, num2)
    print(f"The GCF of {num1} and {num2} is {result}.")
except ValueError:
    print("Please enter valid integers.")
