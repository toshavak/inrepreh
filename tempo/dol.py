def my_generator():
    yield 1
    yield 2
    yield 0.0022844959626743748

# Using the generator function
for value in my_generator():
    print(value)
