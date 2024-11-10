from abc import ABC, abstractmethod

from src.mixin_log import MixinLog


class OriginProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Product(MixinLog, OriginProduct):
    """Информация о свойтвах продуктах"""

    name: str
    description: str
    price: str
    quantity: float

    def __init__(self, name, description, price, quantity):
        # super().__init__(name, description, price)

        # def __init__(self, name, description, price, quantity):
        #     super().__init__(self.__repr__)

        self.name = name
        self.description = description
        self.__price = price
        try:
            self.quantity = quantity
            raise TypeError
        except TypeError as e:
            print(e)
            print("Количество товара = 0")

        super().__init__()

    def __str__(self):
        return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        # return f"{self.name}, {self.description}, {self.price}, {self.quantity}"
        return self.__price

    @price.setter
    def price(self, new_prise: float):
        if new_prise <= 0:
            print("Цена должна быть больше 0")
        else:
            self.__price = new_prise


class Smartphone(Product):
    """Информация о смартфоне"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        efficiency: str
        model: str
        memory: int
        color: str

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError("Складывать можно только объекты Smartphone")
        return (self.price * self.quantity) + (other.price * other.quantity)
        # return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"


class LawnGrass(Product):
    """Информация о Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        country: str
        germination_period: str
        color: str

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError("Складывать можно только объекты LawnGrass")
        return (self.price * self.quantity) + (other.price * other.quantity)
        # return f"{self.name},{self.__price} руб. Остаток: {self.quantity}"


class ShellScriptError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка скрипта."

    def __str__(self):
        return self.message


class ShellScriptEmpty(ShellScriptError):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл пустой."


class ShellScriptShebang(ShellScriptError):
    """Класс исключения при отсутствии shebang"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "В файле отсутствует shebang."
