from .baseveiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {self.veiculo_ligado} | Quantidade de portas: {self.portas}"


    
