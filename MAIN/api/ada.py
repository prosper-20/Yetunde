def division_checker(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if isinstance(a, int) != True:
            print("Cannot divide because a is not a valid integer")
            return
        elif isinstance(b, int) != True:
            print("Cannot divide because b is not a valid integer")

        return func(a, b)
    return inner


@division_checker
def divide(a, b):
    print(a/b)
 
    
divide("abc",5)