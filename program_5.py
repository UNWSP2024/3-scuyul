# Hot Dog Program
import program_2  # make sure program_2 exists and is needed

#Griffin Corniea 9/19/25 Hot Doger

# Prices
TAX_RATE = 0.07
price = 0

# Input hot dog type
hot_dog_type = input("Enter the type of hot dog (Hot Dog / Chili Dog): ").strip().lower()

if hot_dog_type not in ["hot dog", "chili dog"]:
    print("Invalid hot dog type.")
    exit()
elif hot_dog_type == "hot dog":
    price += 3.5
else:
    price += 4.5

# Optional toppings
cheese = input("Add cheese? (yes/no): ").strip().lower()
if cheese == "yes":
    price += 0.5

peppers = input("Add peppers? (yes/no): ").strip().lower()
if peppers == "yes":
    price += 0.75

onions = input("Add grilled onions? (yes/no): ").strip().lower()
if onions == "yes":
    price += 1.0

tax = TAX_RATE * price
total = price + tax
print(f"Total cost: ${total:.2f}")
