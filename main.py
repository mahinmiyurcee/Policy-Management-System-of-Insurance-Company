from Policyholder_class import Policyholder
from Product_class import Product
from Payment_class import Payment

# Create policyholders
policyholder1 = Policyholder(1, "John Doe", "john@example.com")
policyholder2 = Policyholder(2, "Jane Smith", "jane@example.com")

# Create products
product1 = Product(1, "Health Insurance", "Comprehensive health insurance", 100.0)
product2 = Product(2, "Life Insurance", "Term life insurance", 50.0)

# Register policyholders
policyholder1.register()
policyholder2.register()

# Add policies to policyholders
policyholder1.add_policy(product1.name)
policyholder2.add_policy(product2.name)

# Create payments
payment1 = Payment(1, policyholder1.id, 100.0, "2024-08-24")
payment2 = Payment(2, policyholder2.id, 50.0, "2024-08-24")

# Process payments
payment1.process()
payment2.process()

# Display policyholder details
print("\nPolicyholder Details:")
policyholder1.display_details()
print()
policyholder2.display_details()

# Display payment details
print("\nPayment Details:")
payment1.display_details()
print()
payment2.display_details()

# Demonstrate product management
print("\nProduct Management:")
product1.update(price=110.0)
product1.display_details()
print()
product2.suspend()
product2.display_details()