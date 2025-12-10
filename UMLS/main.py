from datetime import datetime as dt

class User:
    """
    Cria um usuário X com idade, nome, senha e login dentro do sistema.
    """
    def __init__(self, age, name, login, password):
        self.__age = age 
        self.__name = name 
        self.__login = login
        self.__password = password
        
    """
    Faz a autenticação do usuário com base no login e na senha do mesmo, caso seja Verdadeiro, retorna true, caso contrário: False
    """
    def authenticate_user(self, login, password):
        if self.__login == login and self.__password == password:
            print("Authenticate User Successfully")
            return True
        else: 
            print("Error in authenticate user.")
            return False
    
    """
    Apresenta o nome do usuário
    """                  
    @property
    def name(self):
        return self.__name 

class Post:
    """
    Cria um post X com id de rastreaemento, titulo, data da publicação e o nome do usuário que publica.
    """
    def __init__(self, id, title, text, publication_date, user):
        self.__id = id 
        self.__title = title
        self.__text = text
        self.__publication_date = self.parse_date(publication_date)
        self.__user = user 
    """
    Converte uma string de data para um objeto datetime;  onde aceita diversos formatos de data
    """
    def parse_date(self, d):
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
            try:
                return dt.strptime(d, fmt)
            except:
                pass
        raise ValueError(f"Invalid date format: {d}")
    
      
    """
    Apresenta o nome do usuário
    """  
    @property
    def publication_date(self):
        return self.__publication_date
          
    """
    Apresenta o titulo da postagem
    """  
    @property
    def title(self):
        return self.__title
         
    """
    Apresenta o conteúdo da postagem 
    """  
    @property
    def text(self):
        return self.__text

    """
    Apresenta o usuário
    """  
    @property
    def user(self):
        return self.__user
  
    """
    Apresenta a representação em string do post no blog
    """  
    def __repr__(self):
        return f"Post({self.__title})"
    
class Blog:
    """
    Listas:
    __posts: armazena todos os posts criados pelo usuário.
    __published_posts: armazena todos os posts postados no blog
    """  
    def __init__(self):
        self.__posts = []
        self.__published_posts = []
    
    """
    Adiciona os posts criados pelo usuário dentro da lista de postagens:
    """
    def add_post(self, post): 
        self.__posts.append(post)
        

    """
    Publica um post que já foi adicionado ao blog.

    O post só é publicado se existir na lista de posts
    e ainda não estiver na lista de posts publicados.
    """    
    def publish_post(self, post):
        if post in self.__posts and post not in self.__published_posts:
            self.__published_posts.append(post)
            return True
        return False
        
    """
    Retorna uma lista de posts já publicados até a data atual.

    A função filtra os posts publicados verificando se a data
    de publicação de cada post é menor ou igual à data de hoje.

    """
    def list_published_posts(self): 
        hoje = dt.now()
        return [p for p in self.__published_posts if p.publication_date <= hoje]
    
    """
    Retorn a lista de todos os posts que estão dentro da lista
    """
    def list_all_posts(self): 
        return self.__posts

    """
    remove um post X do blog, caso ele exista -- é removido; ao contrário, caso ele esteja na lista de posts
    publicados ele também é removido de lá.
    """
    def delete_post(self, post): 
        if post in self.__posts:
            self.__posts.remove(post)
            if post in self.__published_posts:
                self.__published_posts.remove(post)
            return True
        return False
    
user1 = User(35, "Demetrios", "demet244", "123456")
user2 = User(38, "Aluisio", "thi45", "45678")

#tesnting authenticate:
print("\n--- Teste Autenticação ---")
user1.authenticate_user("demet244", "123456")  
user1.authenticate_user("demet244", "wrong")   
user2.authenticate_user("thi45", "45678")      

#create posts:
post1 = Post(1, "A historia de Demetrios Coutinho",  "Atualmente é professor e pesquisador do IFRN",  "12/03/2025", user1)
post2 = Post(2, "A historia de Aluisio Rego", "Atualmente é professor e diretor do NADIC",    "20/03/2023", user2)
post3 = Post(3, "A historia do ifrn",  "Conheça a hiistoria do ifrn por completo", "01/01/2024", user1)
            
#create the blog
my_blog = Blog()

#add posts:
print("------------------------------------------")
print("\n Add Posts")
my_blog.add_post(post1)
my_blog.add_post(post2)
my_blog.add_post(post3)
print("------------------------------------------")

#punlish posts:
print("------------------------------------------")
print("\nPublish Posts ---")
my_blog.publish_post(post1)
my_blog.publish_post(post2)
my_blog.publish_post(post3)
print("------------------------------------------")

#list posts:
print("------------------------------------------")
print("\nAll Posts")
for p in my_blog.list_all_posts():
    print(f"Identification: {p.title}")
    print(f"Autor: {p.user.name}")
    print(f"Data: {p.publication_date.strftime('%d/%m/%Y')}")
    print(f"Conteúdo: {p.text}")
print("------------------------------------------")

#list posts pt2
print("------------------------------------------")
print("\nPublished Posts\n")
for p in my_blog.list_published_posts():
    print(f"Identification: {p.title}")
    print(f"Autor: {p.user.name}")
    print(f"Data: {p.publication_date.strftime('%d/%m/%Y')}")
    print(f"Conteúdo: {p.text}")
print("------------------------------------------")

#delete post
print("------------------------------------------")
print("\nRemove Posts 2")
my_blog.delete_post(post2)
print("------------------------------------------")

# Listando todos os posts após deleção
print("------------------------------------------")
print("\nAll posts after removes")
for p in my_blog.list_all_posts():
    print(f"Identification: {p.title}")
    print(f"Autor: {p.user.name}")
    print(f"Data: {p.publication_date.strftime('%d/%m/%Y')}")
    print(f"Conteúdo: {p.text}")
print("------------------------------------------")
