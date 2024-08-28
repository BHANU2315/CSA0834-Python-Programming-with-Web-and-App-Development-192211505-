def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")
        
        result = num1 / num2
        print("Result of division:", result)
        
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)

divide_numbers()
