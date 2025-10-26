class Product:

      def __init__(self,name="", price=0.0):
            self.name = name
            self.price = price

      def discount(self, percent):
            NewPrice = self.price * (1 - percent /100)
            NewProduct = Product(self.name, NewPrice)
            return NewProduct

      def __mul__(self,quantity):
        return  self.price * quantity
        

      def __repr__(self):
        return f"Produto(nome='{self.name}', preco={self.price:.2f})"

   

   
    

    
    





    