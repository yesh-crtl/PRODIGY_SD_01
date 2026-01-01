temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F/K): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15

elif unit == "F":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15

elif unit == "K":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32

else:
    print("Invalid unit entered. Please enter C, F, or K.")

if unit == "C":
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperature in Kelvin: {kelvin:.2f} K")

elif unit == "F":
    print(f"Temperature in Celsius: {celsius:.2f} °C")
    print(f"Temperature in Kelvin: {kelvin:.2f} K")

elif unit == "K":
    print(f"Temperature in Celsius: {celsius:.2f} °C")
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
