def greet():
    print("Hello! What is your name?")
    name = input()
    print("Nice to meet you, " + name + "! How old are you?")
    age = input()
    print("Great! So you are " + age + " years old.")
    if int(age) >= 18:
        print("You are an adult!")
    else:
        print("You are not yet an adult.")

greet()
