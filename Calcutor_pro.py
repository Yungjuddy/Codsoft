print("Simple Calculator")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")
print("5. Exit")

while True:
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting calculator... Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num_1 = float(input("Please input your first number: "))
            num_2 = float(input("Please input your second number: "))

            if choice == "1":
                print(f"{num_1} + {num_2} = {num_1 + num_2}")
            elif choice == "2":
                print(f"{num_1} * {num_2} = {num_1 * num_2}")
            elif choice == "3":
                if num_2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"{num_1} / {num_2} = {num_1 / num_2}")
            elif choice == "4":
                print(f"{num_1} - {num_2} = {num_1 - num_2}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation != "yes":
                print("Exiting calculator... Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.")
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice. Please try again.")
