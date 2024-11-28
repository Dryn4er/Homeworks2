class MixinLog:

    def __init__(self):
        super().__init__()
        print(repr(self))

#    def __init__(self, name, description, price, quantity):
#        self.name = name
#        self.description = description
#        self.__price = price
#        self.quantity = quantity
#        MixinLog.__init__(self)  # напрямую обращаемся к родителю в инициализацию и отдаём себя, как объект

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.__price}, {self.quantity})"
