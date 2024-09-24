def calculate_tip(bill, service_quality):
    # Define tip percentages
    tip_percentages = {
        'bad': 0.0,
        'okay': 0.15,
        'good': 0.20,
        'great': 0.25
    }

    # Get the corresponding tip percentage
    tip_percentage = tip_percentages.get(service_quality.lower(), 0.0)  # Default to 0% if quality is unknown

    # Calculate the tip
    tip = bill * tip_percentage
    total_amount = bill + tip

    return tip, total_amount

# Example usage
bill_amount = 100  # Example bill amount
service = 'good'   # Example service quality
tip, total = calculate_tip(bill_amount, service)

print(f"Tip: ${tip:.2f}, Total Amount: ${total:.2f}")