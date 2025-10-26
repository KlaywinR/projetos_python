
"""
Pacote loja_iniciante: POO simples com Produto e Carrinho.
Expõe:
- Produto
- Carrinho
"""
from .models import Product
from .cart import Cart
__all__ = ["Produto", "Carrinho"]

