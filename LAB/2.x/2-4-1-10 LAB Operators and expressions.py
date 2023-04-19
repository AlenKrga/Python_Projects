while True:
    x_str = input("Enter a value for x (or 'quit' to exit): ")
    if x_str == 'quit':
        break
    try:
        x = float(x_str)
        y = 3*x**3 - 2*x**2 + 3*x - 1
        print("y =", y)
    except ValueError:
        print("Invalid input, please enter a numeric value or 'quit'.")
