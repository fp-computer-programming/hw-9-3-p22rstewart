# Author RTS 1/17/22

print('Enter the net sales for')

try:
    previous = float(input('- Prior period: '))
    current = float(input('- Current period: '))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result,"and thank you for using the program!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Can't convert a str to a float. Make sure to use a number not a letter!")
finally:
    print("Thank you for using the program!")
