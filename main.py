import time

def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"Function {func.__name__} was run at {time.ctime(start_time)}, with arguments {args}.")
        print(f"Result: {result}, calculated in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

@timer
def find_hypotenuse(a, b):
    c = (a**2 + b**2)**0.5
    return round(c, 2)

a = float(input("Enter the length of the first cathetus: "))
b = float(input("Enter the length of the second cathetus: "))

hypotenuse = find_hypotenuse(a, b)
print(f"The length of the hypotenuse is {hypotenuse}.")