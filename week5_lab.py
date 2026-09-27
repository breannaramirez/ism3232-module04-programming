# week5_lab.py
# Author: Breanna Ramirez
# Business domain: Event ticket order

event_name = "Jazz Festival"
status = "Pending"
quantity = 4
ticket_price = 85.00
is_over_limit = ticket_price * quantity > 1000

print(type(event_name), type(quantity), type(ticket_price), type(is_over_limit))

# Part 2: calculations + f-strings

subtotal = ticket_price * quantity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print("=== Event Ticket Order Summary ===")
print(f"Event:    {event_name}")
print(f"Qty:      {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax:      ${tax:.2f}")
print(f"Total:    ${total:.2f}")
print(f"Requires approval: {requires_approval}")

# Part 3 : user input

user_qty = int(input("Enter a new quantity: "))
new_total = ticket_price * user_qty * 1.07

print(f"New total for {user_qty} tickets: ${new_total:.2f}")
print(f"Requires approval: {new_total > 1000}")
