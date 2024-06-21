from .baseveiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {self.veiculo_ligado} | Tipo: {self.tipo}"

