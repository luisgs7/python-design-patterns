from models import Veiculo, CarroLuxo, CarroPopular, Moto


class VeiculoFactory:
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
