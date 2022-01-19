# Author RTS 1/17/22

def celsius_to_farenheit(temperature,scale):
    
    if str.lower(scale) == "celsius" and s:
        return (temperature * (9/5)) + 32
    elif str.lower(scale) == "fahrenheit":
        return (temperature - 32) * (5/9)
    else:
        return "Sorry, the scale was not inputed correctly. Try again"






while True:
    try:
        number  = float(input("Input a number to be translated into the opposing temperature: "))
        temperature = input("Input a Temperature scale. (Celsius, or Fahrenheit): ")

        print(celsius_to_farenheit(number,temperature))
    except:
        print("Input a number not a Letter!")
        