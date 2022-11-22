x = input("What is your name?")
y = input("What is your age?")
y = int(y)
a = input("We can predict what year it will be when you turn a certain age.  What year would you like to check?")
a = int(a)
z = 2022 + (a-y)
print("Hello " + x + ". " "\nWhen you turn",a,"the year will be:",z)

