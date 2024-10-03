# Customer data processing and report generation (no functions)
customers = int(input("Enter number of customers: "))
total_revenue = 0

for i in range(customers):
    name = input(f"Enter name of customer {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    spent = float(input(f"Enter amount spent by {name}: "))
    
    # Validate data
    if age < 0 or spent < 0:
        print("Invalid data entered.")
        continue
    
    # Apply discount
    if age > 65:
        discount = spent * 0.1
    elif age < 18:
        discount = spent * 0.05
    else:
        discount = 0
    
    spent_after_discount = spent - discount
    print(f"{name} spent ${spent_after_discount:.2f} after discount.")
    
    # Add to total revenue
    total_revenue += spent_after_discount

# Print final report
print(f"Total revenue from all customers: ${total_revenue:.2f}")


# Issues:
# 1. Mixed Responsibilities: Input, validation, discount calculation, and report generation are all mixed together.
# 2. Bug Isolation: If you find an error in the logic, like a discount not being applied correctly or the validation 
#    making it difficult to isolate the problem failing in certain cases, you have to sift through the entire code.
# 3. Repetition: If you need to validate inputs differently in the future or apply a new discount strategy, 
#    you'll have to rewrite large parts of the code.
