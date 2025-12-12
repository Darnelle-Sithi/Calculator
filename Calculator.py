def calculator():
    try: 
        operator = input("Please enter one of the following options [+, -, /, *]: ")
        num_1 = float(input("Please pick your first number here: "))
        num_2 = float(input("Please pick your second number here: "))

        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "/":
            if num_1 == 0 or num_2 == 0:
                result = "Answer is undefined"
                return
            result = num_1 / num_2
        elif operator == "*":
            result = num_1 * num_2
        else:
            print("Invalid operator. Please try again.")
            return
        print(f"The result is: {result}")

    except ValueError:
        print("Incorrect values used. Please use integers.")

calculator()
