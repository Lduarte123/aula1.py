# Entendendo Programação orientada a objetos
# class

# class Pessoa:
#     nome: "1"
#     idade: 0
#     altura: 0

#     def __init__(self, nome, idade, altura) :
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura

#     def getNome (self: str) -> str:
#         return self.nome
    
#     def setNome (self, nome:str):
#         self.nome = nome
#     def getIdade (self: int) -> int:
#         return self.idade
    
#     def setIdade (self, idade:int):
#         self.idade = idade
#     def getNome (self: float) -> float:
#         return self.altura
    
#     def setNome (self, altura:float):
#         self.altura = altura


#     def __str__(self) -> str:
#         return f"nome: {self.nome} \nIdade: {self.idade} \nAltura: {self.altura}"
    
# micaely = Pessoa("Micaely", 23, 1)

# print(micaely.getNome())
# micaely.setNome("Micaely Santos")
# print(micaely)





#crie uma classe chamada cachorro
#este cachorro tem is seguintes atributos
# nome, raça, cor, idade e altura

#instacie 3 cachorros

class Cao:
    # nome = "_"
    # raca = "_"
    # cor = "-"
    # idade = 0
    # altura = 0

    def __init__(self, nome, raca, cor, idade, altura):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.altura = altura
        

    
    def getNome (self) -> str:
        return self.nome
    
    def setNome (self, nome:str):
        self.nome = nome

    def getraca (self) -> str:
        return self.raca
    
    def setRaca (self, raca:str):
        self.raca = raca

    def getCor (self) -> str:
        return self.cor
    
    def setCor (self, cor:str):
        self.cor = cor

    def getIdade (self) -> int:
        return self.idade
    
    def setIdade (self, idade:int):
        self.idade = idade
    
    def getAltura (self) -> float:
        return self.altura
    
    def setAltura (self, altura:float):
        self.altura = altura

    def __str__(self) -> str:
         return f"nome: {self.nome} \nRaça:{self.raca} \nCor: {self.cor} \nIdade: {self.idade} \nAltura: {self.altura}"


cachorro1 = Cao("Rex", "Pincher", "preto", 12, 0.67)   
print(cachorro1)

class Carro:
    def __init__(self, nome, fabricante, ano, valor , chassi, placa):
        self.nome = nome
        self.frabricante = fabricante
        self.ano = ano
        self.valor = valor
        self.chassi = chassi
        self.placa = placa
    
    def getNome (self: str) -> str:
        return self.nome 
        
    def getFabricante (self: str) -> str:
        return self.nome 
        
    def getNome (self: str) -> str:
        return self.nome 
        
    def getNome (self: str) -> str:
        return self.nome 
        
    def getNome (self: str) -> str:
        return self.nome 
        
    def getNome (self: str) -> str:
        return self.nome 
        
    def getNome (self: str) -> str:
        return self.nome 
        