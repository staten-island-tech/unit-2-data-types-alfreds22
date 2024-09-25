def calculate_tip():
    bill_amount = float(input("Enter the total bill amount: $"))
    service_quality = input("How was the service? (excellent, good, average, poor):")
    if service_quality == "excellent":
        tip_percentage = 0.20
    elif service_quality == "good":
        tip_percentage = 0.15
    elif service_quality == "average":
        tip_percentage = 0.10
    elif service_quality == "poor":
        tip_percentage = 0.05
    else:
        print("Invalid input for service quality. Please enter excellent, good, average, or poor.")
        return
    tip_amount = bill_amount * tip_percentage
    total_amount = bill_amount + tip_amount
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount to pay: ${total_amount:.2f}")
calculate_tip()
