def greet(name, greeting= "Hello"):

    print(f"{greeting}, {name}!")

greet("Alex")
    
#call with a name and custom greeting
greet("Alex", "Good morning")
    
#greeting passed as a keyword argument
greet(name="Alex", greeting="Hello")
    


