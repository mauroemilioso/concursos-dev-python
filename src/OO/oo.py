class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()


# Herarquia de classes ---------------------------------------------
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz: Miau!")

# Criando instâncias das subclasses
cachorro = Cachorro()
gato = Gato()

cachorro.fazer_som()  # Saída: O cachorro faz: Au Au!
gato.fazer_som()      # Saída: O gato faz: Miau!


# exemplo de sobrescrita de método em python -------------------------
class Veiculo:
    def ligar(self):
        print("Veículo ligado.")

class Carro(Veiculo):
    def ligar(self):
        super().ligar()  # Chamando o método da superclasse
        print("Carro pronto para rodar.")

# Criando uma instância da classe Carro
meu_carro = Carro()
meu_carro.ligar()

