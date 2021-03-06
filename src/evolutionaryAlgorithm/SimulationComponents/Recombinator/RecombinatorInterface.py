from abc import abstractmethod
from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentInterface import SimulationComponentInterface


class RecombinatorInterface(SimulationComponentInterface):
    @abstractmethod
    def recombine(self, population: List[List[IndividualInterface]]):
        pass
