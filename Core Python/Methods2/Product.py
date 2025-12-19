""""Q2. Design a class Product that:
*Maintains a base tax rate applicable to all products.
*Each product has a name and base price.
*Has a method to compute final price including tax.
*Can change tax rate for all products using one method.
*Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.Creating multiple products.
2.Changing the tax rate.
3.Showing updated prices and validity checks."""""

class Product:
    base_tax_rate=0.2
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def final_price(self):
        return self.price+(self.price*Product.base_tax_rate)
    @classmethod
    def change_tax(cls,new_tax_rate):
        cls.base_tax_rate=new_tax_rate
    @staticmethod
    def check_price(price):
        if price<100:
            return "negative"
        else:
            return "realistic"
p=Product("oil",100)
p2=Product("powder",0)
print(p.final_price())
print(p.check_price(120))
print(p.check_price(80))
Product.change_tax(0.5)
print(p.final_price())

