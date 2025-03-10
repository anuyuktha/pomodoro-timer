def calculator():
    while True:
        print("\nCalculator")
        print("Enter the mathematical expression you want to calculate")
        print("Type 'exit' to quit the calculator.")
        num= input("Expression: ")

        if expression.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        if not re.match(r'^[\d+\-*/.]+$', num):
                print("Invalid expression")
                continue
        try:
            result = eval(num) 
            print(f"Result: {result}")
        except:
            print("Invalid expression")
       

calculator()
