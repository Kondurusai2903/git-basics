class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def details(self):
        print(f"ths car name is ${self.name} and the model is ${self.model}")


bmw = Car('bmw', "k2f")
bmw.details()
