class Item:

    " Grocery list item "

    def __init__(self, name, price_without_cut, cut_percentage, category,
                 vat_percentage, quantity, ingredients):
        self.name = name
        self.price_without_cut = price_without_cut
        self.cut_percentage = cut_percentage
        self.category = category
        self.vat_percentage = vat_percentage
        self.quantity = quantity
        self.ingredients = ingredients

    def get_total_price(self):
        return self.price_without_cut*(1+self.vat_percentage/100)*(1-self.cut_percentage/100)*self.quantity

    def get_total_vat(self):
        return self.price_without_cut*self.vat_percentage/100*(1-self.cut_percentage/100)*self.quantity

    def get_total_cut(self):
        return self.price_without_cut*(1+self.vat_percentage/100)*self.cut_percentage/100*self.quantity

    def __repr__(self):
        return f"{self.name:s} x {self.quantity:d}"

if __name__ == "__main__":
    beef = Item("Beef", 12.3, 0, "Meat", 10, 2, ["Beef"])
    print(beef)
    print(f"Total cut   : {beef.get_total_cut():.2f} \u20ac ")
    print(f"Total price : {beef.get_total_price():.2f} \u20ac ")
    print(f"Total VAT   : {beef.get_total_vat():.2f} \u20ac ")
