# List of banned users
banned_users = ["john", "alice", "viktor"]

# Ask if the user has an invitation
invited = input("Do you have an invitation? (yes/no): ").strip().lower()

# Ask if the user has paid
paid = input("Did you pay for the entry? (yes/no): ").strip().lower()

# Access is allowed if invited OR paid
if invited == "yes" or paid == "yes":
    # Ask for the user's name
    name = input("What's your name? ").strip().lower()

    # Check if the name is not in the banned list
    if name not in banned_users:
        print("✅ Access granted. Welcome!")
    else:
        print("⛔ Access denied. You are on the banned list.")
else:
    print("⛔ Access denied. You need an invitation or payment to enter.")
