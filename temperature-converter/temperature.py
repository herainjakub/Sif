# Program na převod teploty ze stupňů Celsia na Fahrenheity a Kelviny

celsius = float(input("Zadejte teplotu ve stupních Celsia: "))

fahrenheit = round(celsius * 9 / 5 + 32, 2)
kelvin = round(celsius + 273.15, 2)

print(f"{celsius} °C = {fahrenheit} °F = {kelvin} K")