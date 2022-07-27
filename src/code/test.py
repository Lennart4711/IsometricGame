class Test:
    def __init__(self):
        self.x = "asd"


test = Test()


def change(test):
    test.x = "wasd"


change(test)
print(test.x)
