from typing import List

from src.evolutionaryAlgorithm.SimulationComponents.Individual.IndividualInterface import IndividualInterface
from src.evolutionaryAlgorithm.SimulationComponents.SurviviorSelector.SurviviorSelectorInterface import \
    SurviviorSelectorInterface
from src.evolutionaryAlgorithm.SimulationComponents.Individual.impl.FloatingPointIndividual import \
    FloatingPointIndividual


class eliteSurvivor(SurviviorSelectorInterface):

    def __init__(self):
        pass

    def selectSurvivor(self, population: List[IndividualInterface], offspring: List[IndividualInterface]) -> \
            List[IndividualInterface]:

        t = len(population)/2
        newGeneration = []

        fitness = []
        for el in population:
            fitness.append(el.getFitnessFunctionEvaluation())

        for i in range(int(t)):
            k = fitness[0]
            index = 0
            for j in range(len(fitness)):
                if k > fitness[j]:
                    k = fitness[j]
                    index = j
            del(fitness[index])
            newGeneration.append(FloatingPointIndividual(population[index].getRepresentation()))
            del(population[index])

        fitness = []
        for el in offspring:
            fitness.append(el.getFitnessFunctionEvaluation())

        for i in range(int(t)):
            k = fitness[0]
            index = 0
            for j in range(len(fitness)):
                if k > fitness[j]:
                    k = fitness[j]
                    index = j
            del(fitness[index])
            newGeneration.append((FloatingPointIndividual(offspring[index].getRepresentation())))
            del(offspring[index])

        return newGeneration
