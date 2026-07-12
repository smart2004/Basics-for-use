try:
    x = 10/0
except ZeroDivisionError:
    print('unable divide by Zero')
finally:
    print("that's it")
