class Product:

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price


class DiscountProduct(Product):

    def __init__(self, name: str, price: float, discount: float):
        super().__init__(name, price)
        self._discount = discount

    @property
    def price(self) -> float:
        return self._price - self._discount * self._price


class Register:

    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def sum(self) -> float:
        result = 0.0
        for product in self.products:
            result += product.price
        return result


my_register = Register()

my_register.add_product(DiscountProduct('usb', 500.00, 0.10))
my_register.add_product(DiscountProduct('tv', 2000.00, 0.10))
my_register.add_product(DiscountProduct('dvd', 1000.00, 0.10))

print(my_register.sum())
