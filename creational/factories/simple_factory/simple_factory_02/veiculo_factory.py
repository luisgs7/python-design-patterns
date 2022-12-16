from models import Veiculo, CarroLuxo, CarroPopular, Moto


class VeiculoFactory:
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        elif tipo == "popular":
            return CarroPopular()
        elif tipo == "moto":
            return Moto()
        else:
            return "Veiculo não existe."

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()
