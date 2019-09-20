class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coordinates(self):
        print(f'Coordinates x {self.x} y {self.y}')
    
    def __repr__(self):
        return f'Object point x: {self.x} y: {self.y}'

my_point = Point(10,20)

my_point.coordinates()
print(my_point)

my_point2 = Point(30,30)
print(my_point2)

class Product:
    def __init__(self, name, price, stock = 0,discount = 0, max_discount = 0):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Name can not be less then 2 symbols')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Discount is too big')
        if self.discount > self.max_discount:
            self.discount = self.max_discount
    
    def discounted(self):
        return self.price * self.discount / 100
    
    def sell(self, items_count = 1):
        if items_count > self.stock:
            raise ValueError("Not enought items")
        self.stock -=items_count
    
    def __repr__(self):
        return f'<Product name {self.name}>'
    def get_color(self):
        raise NotImplementedError

product1 = Product('Smth', 100)

class Phone(Product):
    def __init__(self, name, price, color, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'
    
    def get_color(self):
        return f'Color {self.color}'

class Sofa(Product):
    def __init__(self, name, price, color, texture, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color
        self.texture = texture
    
    def get_color(self):
        return f'Sofa color {self.color}'

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'

phone = Phone('iPhone Xs', 100, 'серый')
print(phone.color)

sofa1 = Sofa('Big sofa',25312.4, 'yellow', 'velours')
print(sofa1)
print(sofa1.color)
print(phone.get_color())
print(sofa1.get_color())







