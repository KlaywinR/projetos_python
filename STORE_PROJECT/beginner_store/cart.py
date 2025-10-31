from beginner_store.models import Product

class Cart:
        """Carro de compra simples"""
       
        def __init__(self):
         self.itens = []
        
        """
            Acrescenta (produto, int (quantidade=1)) em itens.
        """
        def add(self, product, quantity=1):
            self.itens.append((product, quantity))
        
            """]__
            Remove a primeira ocorrência de 'produto' em itens. 
            Se o produto aparecer varias vezes, apague a primeira e pare.
            """
        def  remove(self, product):
            for i , (p,q) in enumerate(self.itens):
                if p == product: #comparacao de nome
                    del self.itens[i]
                break

            """
            Retorna apenas os nomes dos produtos sem repeticão, na ordem 
            de primeira aparição
            """
    
        def UniqueItens(self):
            vistos = []
            for product, _ in self.itens:
                if product not in vistos:
                    vistos.append(product)
                return vistos 
            """
            Soma todos os subtotais usando a definição:
            subtotal = produto * quantidade
            Retorna float em reais.
            """   
        def total(self):
            total = 0.0
            for product, quantidade in self.itens:
             total += product.price * quantidade
            return total
        
            """
            Linhas para tabulate:
            ["Produto", "Preço", "Qtd", "Subtotal"]
            """      
        def table_lines(self):
            lines  = []
            for product, quantity in self.itens:
                subtotal  = product * quantity
                line = [product.name , f"Preço em Reais: {product.price:.2f}", quantity, f"R$ {subtotal:.2f}"]
                lines.append(line)
                return lines
           
##!------------------------------------------------ 
            """
            Retorna um novo carrinho com "produto" adicionado a quant.
            1 - Não altera o carrinho original
            """
        def __add__(self, product):
            NewCart = Cart()
            NewCart.itens = self.itens.copy()
            NewCart.add(product, 1)
            return NewCart
        
            """
            Retorna um carrinho com a PRIMEIRA ocorrência de produto removida
            Não altera o carrinho original
            """
        def __sub__(self, product):
            newCart = Cart()
            newCart.itens = self.itens.copy()
            newCart.remove(product)
            return newCart
        
            """
            Operador em lugar += produto.
            Deve adicionar o produto ao propio carrinho e retornar self. 
            """
        def __iadd__(self, product):
            self.add(product, 1)
            return self
        
            """
            Operador em lugar: carrinho -= produto.
            Deve REMOVER a PRIMEIRA ocorrência do próprio carrinho e retornar self.
            """
        def __isub__(self, product):
            self.remove(product)
            return self
    


                
        
            
            
            
            
        
            
            
        
        
            

        
    
        
