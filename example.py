def one():
    print("one was called")
def two():
    print("two was called")
def default():
    print("defaulting")
funcs = {"one": one , "two": two}
choice = input("which expression ")
result = funcs.get(choice,default)()