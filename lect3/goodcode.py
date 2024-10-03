# Function to validate customer data
def validate_customer_data(age, spent):
    return age >= 0 and spent >= 0

# Function to calculate discount based on age
def calculate_discount(age, spent):
    if age > 65:
        return spent * 0.1  # 10% discount for seniors
    elif age < 18:
        return spent * 0.05  # 5% discount for minors
    return 0  # No discount

# Function to process a single customer and return the final amount they spent
def process_customer(name, age, spent):
    if not validate_customer_data(age, spent):
        print(f"Invalid data for {name}. Skipping customer.")
        return 0
    
    discount = calculate_discount(age, spent)
    spent_after_discount = spent - discount
    print(f"{name} spent ${spent_after_discount:.2f} after discount.")
    return spent_after_discount

# Function to process all customers and calculate total revenue
def generate_report(customers_data):
    total_revenue = 0

    for customer in customers_data:
        name, age, spent = customer['name'], customer['age'], customer['spent']
        total_revenue += process_customer(name, age, spent)
    
    return total_revenue

# Main program execution: input gathering and output display
# Input: Gather the number of customers and customer data
customers = int(input("Enter number of customers: "))
customers_data = []

for i in range(customers):
    name = input(f"Enter name of customer {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    spent = float(input(f"Enter amount spent by {name}: "))
    customers_data.append({'name': name, 'age': age, 'spent': spent})
    
# Generate the report based on the gathered data
total_revenue = generate_report(customers_data)

# Output: Display the final total revenue
print(f"Total revenue from all customers: ${total_revenue:.2f}")

# Modular Design: Each function handles a specific responsibility.

# Advantages of Modular Code for Bug Detection:

# 1. Easy to find and correct bugs: If there's a bug, say, in the discount calculation, 
# you only need to check the calculate_discount() function rather than combing through the entire code. 

# 2. Simpler Testing: You can easily write unit tests for individual functions like process_customer(), 
# calculate_discount(), and validate_customer_data(), which makes it easy to catch bugs in small, manageable parts of the program.

# 3. Maintainability: You can update specific parts (like a new discount policy) without affecting the entire 
#    flow of the program.
