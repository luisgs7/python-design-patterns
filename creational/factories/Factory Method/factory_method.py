"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from random import choice
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto está buscando o cliente...")


class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
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


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "popular":
            return CarroPopular()
        assert 0, "Veículo não existe"


if __name__ == "__main__":
    carros_disponiveis_zona_norte = ["luxo", "popular", "moto"]

    print("Zona Norte")
    for i in range(10):
        carro = ZonaNorteVeiculoFactory.get_carro(choice(carros_disponiveis_zona_norte))
        carro.buscar_cliente()

    carros_disponiveis_zona_sul = ["popular"]

    print("\nZona Sul")
    for i in range(10):
        carro = ZonaSulVeiculoFactory.get_carro(choice(carros_disponiveis_zona_sul))
        carro.buscar_cliente()
