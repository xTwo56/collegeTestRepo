def kawaii(func: callable):
    def Wrap():
        print("**** Kawaii! ****")
        dio = func()
        print("**** Kawaii! ****")
        return dio
    return Wrap

