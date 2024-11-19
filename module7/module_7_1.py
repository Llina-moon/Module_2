class Product:

    def __init__(self, name: str, weight: bool, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:

    def __init__(self) -> None:
        self.__file_name = "products.txt"

    def get_products(self):
        with open(self.__file_name, "r") as file:
            products = file.read()
            return products

    def add(self, *products: Product):
        current_products = self.get_products()

        with open(self.__file_name, 'a') as file:
            for product in products:
                if str(product) not in current_products:
                    file.write(f"{product}\n")
                    current_products = current_products + f"{product}\n"
                else:
                    print(f'Продукт {product} уже есть в магазине')


sh = Shop()

p0 = Product('Potato', 50.5, 'Vegetables')
p1 = Product('Milk', 2, 'Vegetables')
p2 = Product('Milk', 2, 'Vegetables')
p3 = Product('Beer', 3, 'Vegetables')

sh.add(p0, p1, p2, p3)
