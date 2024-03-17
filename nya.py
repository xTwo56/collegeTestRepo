def kawaii(func):
    def Wrap():
        print("**** Kawaii! ****")
        dio = func()
        print("**** Kawaii! ****")
        return dio
    return Wrap

@kawaii
def hello():
    print("Hello, World!")

hello()
