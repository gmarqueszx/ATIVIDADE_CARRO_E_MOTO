class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
    
    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {self.veiculo_ligado}"
    
    def ligar_veiculo(self):
        self._ligado = True
        
    @property
    def veiculo_ligado(self):
        return 'Sim' if self._ligado else 'Não'

