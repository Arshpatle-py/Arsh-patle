from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
   c = float(input("Enter temperature in Celsius: "))
   result = celsius_to_fahrenheit.convert(c)
   print("Temperature in Fahrenheit:", result)

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius.convert(f)
    print("Temperature in Celsius:", result)

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    result = celsius_to_kelvin.convert(c)
    print("Temperature in Kelvin:", result)

else:
    print("Invalid choice!Kindly choose a number between 1-3")
