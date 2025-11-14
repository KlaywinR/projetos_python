class Vehicle:
    def move(self):
        pass   
    
class Motorized():
    def start_engines(self):
        print("Os motores do Tesla de Demetrios estão sendo ligados...")
           
class Eletric():
    def charging_battery(self):
        print("A bateria do tesla de Demetrios está recebendo carga - (67% de 100%)")
        
    def eletric_engines(self):
        print("Os motores do tesla de Demetrios estão sendo ligados - (OFF --> ON)")  
           
class Car(Vehicle, Motorized):
    def move(self):
        print("O veiculo está se movendo nas ruas de Pau dos Ferros - RN")
        print("Situação da Bicicleta: Em uso")
        
class CarEletric(Motorized, Vehicle, Eletric):
    def move(self):
        print("Demetrios está se movendo com o tesla")
        
class Bike(Vehicle):
    def move(self):
        print("Demetrios está andando em uma bicicleta pelas ruas de Pau dos Ferros - RN")
        
        
print("\n----------------------------")
print("TESTANDO O CARRO ELETRICO \n")
car_eletric_example = CarEletric()
car_eletric_example.charging_battery()
car_eletric_example.eletric_engines()
print("-----------------------------")
    

print("\nTesting the Bike Class")
bike1 = Bike()
bike1.move()
print("----------------------------")

print("\nTesting the class car")
car1 = Car()
car1.move()
print("----------------------------")

print("\nTESTING THE MOTORIZED CLASS")
example = Motorized()
example.start_engines()
print("----------------------------")

              