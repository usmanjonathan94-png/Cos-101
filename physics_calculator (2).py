while True:
    print("\n===== MY PHYSICS CALCULATOR =====")
    print("1. Work Done")
    print("2. Weight")
    print("3. Speed")
    print("4. Force")
    print("5. Kinetic Energy")
    print("6. Exit")

    option = input("\nChoose an option (1-6): ")

    if option == "1":
        print("\n--- WORK DONE ---")
        f = float(input("Enter force: "))
        d = float(input("Enter distance: "))
        result = f * d
        print("Work Done =", result, "Joules")

    elif option == "2":
        print("\n--- WEIGHT ---")
        m = float(input("Enter mass: "))
        g = 9.8
        result = m * g
        print("Weight =", result, "Newtons")

    elif option == "3":
        print("\n--- SPEED ---")
        d = float(input("Enter distance: "))
        t = float(input("Enter time: "))
        if t != 0:
            result = d / t
            print("Speed =", result, "m/s")
        else:
            print("Time cannot be zero!")

    elif option == "4":
        print("\n--- FORCE ---")
        a = float(input("Enter acceleration: "))
        m = float(input("Enter mass: "))
        result = m * a
        print("Force =", result, "Newtons")

    elif option == "5":
        print("\n--- KINETIC ENERGY ---")
        v = float(input("Enter velocity: "))
        m = float(input("Enter mass: "))
        result = 0.5 * m * v ** 2
        print("Kinetic Energy =", result, "Joules")

    elif option == "6":
        print("\nThanks for using my Physics Calculator!")
        break

    else:
        print("\nInvalid option! Try again.")
