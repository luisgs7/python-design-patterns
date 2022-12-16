from random import choice
from veiculo_factory import VeiculoFactory

if __name__ == "__main__":
    carros_disponiveis = ["luxo", "popular", "moto"]

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()
