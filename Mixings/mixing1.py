from ALURA.main import Employee
class AuthenticableMixing:    
    def authentic(self, password):
        if password == self.password:
            print("Autenticação Válida")
        else:
            print("Autenticação Falhou!")

class AtendimentoMixing:
    
    def __init__(self, client_name):
        self.client_name = client_name
        self.atendimentos = []

    def register_service(self):
        print("\n== Cadastro de Atendimento ===")
        name_client = input("Nome do Cliente: ")
        phone = input("Telefone: ")
        reason = input("Motivo do Atendimento: ")
        
        service = {
            "name_client": name_client,
            "phone": phone,
            "reason": reason
        }
        
        self.atendimentos.append(service)
        
        print("O atendimento foi um sucesso!")

    def costumer_service(self):
        print(f"\nOlá, {self.client_name}! Bem-vindo ao nosso sistema de atendimento virtual.")
        print("Por favor, escolha uma opção:")
        print("1 - Ver status do pedido")
        print("2 - Falar com atendente")
        print("3 - Criar reclamação")
        print("4 - Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            self.ver_pedido()

        elif opcao == "2":
            self.falar_atendente()

        elif opcao == "3":
            self.registrar_reclamacao()

        elif opcao == "4":
            print("Obrigado por usar o nosso sistema, tenha um ótimo dia!")
            return 

        else:
            print("Opção inválida. Tente novamente.")
            self.costumer_service()

    def ver_pedido(self):
        print(f"{self.client_name}, o seu pedido está em rota de entrega.")
        self.costumer_service()

    def falar_atendente(self):
        print(f"{self.client_name}, você será direcionado para um dos nossos atendentes...")
        self.costumer_service()

    def registrar_reclamacao(self):
        reclamacao = input("Digite sua reclamação: ")
        print("Reclamação registrada com sucesso!")
        self.costumer_service()



class OvertimeMixing:
    def calculate_overtime(self, hours):
        if hours > 8:
            return hours - 8
        return  0
       
class Manager(Employee, AuthenticableMixing, OvertimeMixing):
    pass

class Director(Employee, AuthenticableMixing):
    pass

class Client(AuthenticableMixing):
    pass

class Clerk(Employee, AtendimentoMixing):
    def __init__(self, name, salary, client_name):
        Employee.__init__(self, name, salary)
        AtendimentoMixing.__init__(self, client_name)



if __name__ == "__main__":
    
    print("\n -- Testing Manager Class -- ")
    m1 = Manager("Antonio", 8000)
    m1.password = "123456"
    m1.authentic("123456")
    print("Horas Extras: ", m1.calculate_overtime(10))
    
    
    print("\n == Testing the Class Director ==")
    director_one = Director("Marina", 15000)
    director_one.password = "admin"
    director_one.authentic("admin")
    
    print("\n -- Tesnting Client --")
    client = Client()
    client.password = "client12345"
    client.authentic("client12345")
    
    
    print("\n -- Testando o Atendimento -- ")
    clerk_one = Clerk("Joao", 2500, "Demetrios")

    
    print("\n -- Atendimento Virtual --")
    clerk_one.costumer_service()
    
    print("\n -- Resgistrando um determinado atendimento --")
    clerk_one.register_service()
    
    print("\n --T odos os atendimentos resgistrados --")
    print(clerk_one.atendimentos)
    