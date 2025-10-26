print("🎯 Interactive Calculator")
print("========================")

while True:
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)") 
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Goodbye! 👋")
        break
        
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"🔹 {num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"🔹 {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"🔹 {num1} × {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("❌ Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"🔹 {num1} ÷ {num2} = {result}")
        except:
            print("❌ Invalid input! Please enter numbers.")
    else:
        print("❌ Invalid choice! Please try again.")
