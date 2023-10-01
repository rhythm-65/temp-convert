print("Enter 1 to convert to Celsius and 2 to convert into fahrenheit:")
choice=int(input())
if choice==1:
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  celsius = (fahrenheit - 32) * 5/9
  print("Temperature in Celsius:", celsius)
else:
  celsius=float(input("Enter the temperature in Celsius:"))
  fahrenheit=(9*celsius/5)+32
  print("Temperature in Fahrenheit:",fahrenheit)
              
