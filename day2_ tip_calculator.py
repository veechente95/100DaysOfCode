print("Welcome to the tip calculator!")

total_bill = float(input("What was the total of the bill?: "))
split_bill = int(input("How many people to split the bill?: "))
tip = int(input("What percentage tip would you like to leave?: "))
per_person = round(total_bill / split_bill + ((total_bill * tip) / 100), 2)

print(f"Each person should pay {per_person}")
