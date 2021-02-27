class Product:

    # construtor to set data
    def __init__(self, id, name, brand, price, discount):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.discount = discount

        # function to show data
    def show(self):
        print("product id: ",self.id)
        print("product name: ",self.name)
        print("product brand: ",self.brand)
        print("product price:",self.price)
        print("product discount: ",self.discount)

    def calc(self,price,discount):
        dis=(price-(price*discount/100))
        print("the final price of the product: ",dis)

n=int(input("enter the size"))
for i in range(1,n+1):
    id= int(input("enter the id"))
    name = input("enter the name")
    brand = input("enter the brand")
    price = float(input("enter the price"))
    discount = float(input("enter the discount"))
    p1 = Product(id,name,brand,price,discount)


#create object
    p1.show()
    p1.calc(price,discount)





