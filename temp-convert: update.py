print("Enter the temperature of each patient (separated by commas):")
temp_input = input()
temp_list = temp_input.split(",")
temperatures = [float(temp) for temp in temp_list]

print("Enter 1 to convert to Celsius and 2 to convert into Fahrenheit:")
choice = int(input())

if choice == 1:
    celsius_list = [(temp - 32) * 5/9 for temp in temperatures]
    print(f"Temperatures in Celsius: {celsius_list}")
    for i in range(len(celsius_list)):
        if celsius_list[i] < 37:
            print(f"Patient {i+1} has a normal cough.")
            print("Medical advice: Rest and drink plenty of fluids.")
        elif celsius_list[i] < 38:
            print(f"Patient {i+1} has a low fever.")
            print("Medical advice: Rest and drink plenty of fluids. Take over-the-counter medication such as acetaminophen or ibuprofen.")
        elif celsius_list[i] < 39:
            print(f"Patient {i+1} has a high fever.")
            print("Medical advice: Rest and drink plenty of fluids. Take over-the-counter medication such as acetaminophen or ibuprofen. Seek medical attention if the fever persists or worsens.")
        else:
            print(f"Patient {i+1} needs severe treatment.")
            print("Medical advice: Seek immediate medical attention.")
elif choice == 2:
    fahrenheit_list = [(temp * 9/5) + 32 for temp in temperatures]
    print(f"Temperatures in Fahrenheit: {fahrenheit_list}")
    for i in range(len(fahrenheit_list)):
        if fahrenheit_list[i] < 98.6:
            print(f"Patient {i+1} has a normal cough.")
            print("Medical advice: Rest and drink plenty of fluids.")
        elif fahrenheit_list[i] < 100.4:
            print(f"Patient {i+1} has a low fever.")
            print("Medical advice: Rest and drink plenty of fluids. Take over-the-counter medication such as acetaminophen or ibuprofen.")
        elif fahrenheit_list[i] < 102.2:
            print(f"Patient {i+1} has a high fever.")
            print("Medical advice: Rest and drink plenty of fluids. Take over-the-counter medication such as acetaminophen or ibuprofen. Seek medical attention if the fever persists or worsens.")
        else:
            print(f"Patient {i+1} needs severe treatment.")
            print("Medical advice: Seek immediate medical attention.")
else:
    print("Invalid choice")
