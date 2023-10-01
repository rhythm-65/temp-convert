print("Enter 1 to convert to Celsius and 2 to convert into fahrenheit:")
choice=int(input())
if choice==1:
  while True:
        fahrenheit_input = input("Enter temperature(s) in Fahrenheit (separated by commas): ")
        if fahrenheit_input.lower() == "done":
            break
        fahrenheit_list = fahrenheit_input.split(",")
        for fahrenheit in fahrenheit_list:
            celsius = (float(fahrenheit) - 32) * 5/9
            print(f"{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius")
elif choice == 2:
    while True:
        celsius_input = input("Enter temperature(s) in Celsius (separated by commas): ")
        if celsius_input.lower() == "done":
            break
        celsius_list = celsius_input.split(",")
        for celsius in celsius_list:
            fahrenheit = (float(celsius) * 9/5) + 32
            print(f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit")
else:
    print("Invalid choice")
              
