menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {
    "Burger": 3,
    "Fries": 3,
    "Chicken": 1,
    "Drink": 2
}

DISCOUNT_THRESHOLD = 500
DISCOUNT_RATE = 0.10

print("===== BILL =====")

total = 0
for item, quantity in orders.items():
    subtotal = menu[item] * quantity
    total += subtotal
    print(f"{item:<10} {quantity} x {menu[item]:>4} = {subtotal:>7.2f}")

print("-" * 32)
print(f"{'Total:':<22}{total:>10.2f}")

discount = 0
if total >= DISCOUNT_THRESHOLD:
    discount = total * DISCOUNT_RATE
    print(f"{'Discount (10%):':<22}{discount:>10.2f}")

final_total = total - discount
print(f"{'Amount to pay:':<22}{final_total:>10.2f}")

payment = float(input("\nEnter customer payment: "))

while payment < final_total:
    print("Insufficient payment!")
    payment = float(input("Enter customer payment: "))

change = payment - final_total
print(f"{'Payment:':<22}{payment:>10.2f}")
print(f"{'Change:':<22}{change:>10.2f}")
