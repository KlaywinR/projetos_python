from tabulate import tabulate 
from beginner_store.models import Product
from beginner_store.cart import Cart

def main():
    
    notebook = Product("Caderno Tilibra", 25.00)
    school_eraser = Product("Borracha Stitch", 7.00)
    pencil = Product("Lapis Faber Castell", 5.00)
    
    """
    Deesconto de 20% no valor do caderno 
    """
    promotion_notebook = notebook.discount(20)

##** CARRINHO BASE:

    MyBaseCart = Cart()
    MyBaseCart.add(notebook, 2)
    MyBaseCart.add(pencil,8)
    MyBaseCart.add(school_eraser, 10)
    
##* TESTANDO OPERADORES:

    MyCart2 = MyBaseCart + promotion_notebook
    MyCart3 = MyCart2 - pencil
    MyBaseCart += pencil
    MyBaseCart -= school_eraser
    
##* MOSTRANDO O CAMINHO FINAL:

    header = ["Products", "Prices", "Quantity", "SubTotal"]
    print(tabulate(MyCart3.table_lines(), headers=header, tablefmt="grid"))
    
    print("\nTotal carrinho 3: R$ {:.2f}".format(MyCart3.total()))
    print("Itens únicos carrinho 3:", [p.name for p in MyCart3.UniqueItens()])



if __name__ == "__main__":
    main()


   