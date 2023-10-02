try:
    num = int(input("Enter numerator : "))
    den = int(input("Enter denominator : "))
    print(num/den)
except ZeroDivisionError:
    print("Please enter a non-zero denominator")
except ValueError:
    print("Please enter an integer value")
print("program end")
# we can raise an exception on our own by using the 'raise' keyword, it is useful when we
# want to test our handling of exceptions
