menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {}

DISCOUNT_THRESHOLD = 500
DISCOUNT_RATE = 0.10

def show_menu():
    print("===== CANTEEN MENU =====")
    for item, price in menu.items():
        print(f"{item:<10} - {price}")

def take_orders():
    number = int(input("\nEnter number of order attempts: "))

    for i in range(1, number + 1):
        print("\nOrder", i)

        item = input("Enter item name: ").title()

        if item not in menu:
            print("Item not available!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity!")
            continue

        orders[item] = orders.get(item, 0) + quantity

def show_order_summary():
    print("\n===== ORDER SUMMARY =====")
    for item, quantity in orders.items():
        print(item, "x", quantity)

def compute_bill():
    print("\n===== BILL =====")

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
    return final_total

def process_payment(final_total):
    payment = float(input("\nEnter customer payment: "))

    while payment < final_total:
        print("Insufficient payment!")
        payment = float(input("Enter customer payment: "))

    change = payment - final_total
    print(f"{'Payment:':<22}{payment:>10.2f}")
    print(f"{'Change:':<22}{change:>10.2f}")

def main():
    show_menu()
    take_orders()

    if not orders:
        print("\nNo valid orders were placed.")
        return

    show_order_summary()
    final_total = compute_bill()
    process_payment(final_total)
    print("\nThank you for ordering!")

main()
