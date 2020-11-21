from src.evolutionaryAlgorithm.SimulationComponents.SimulationComponentFactoryInterface import \
    SimulationComponentFactoryInterface


class RecombinatorFactory(SimulationComponentFactoryInterface):
    @staticmethod
    def validate(config: dict):
        pass

    @staticmethod
    def build(config: dict) -> InitializatorInterface:
        recombinator = config["Recombinator"]
        if recombinator["Type"] == "singlePointRecombinator":
            return singlePointRecombinator()
        elif recombinator["Type"] == "twoPointRecombinator":
            return twoPointRecombinator
        elif recombinator["Type"] == "averageRecombinator":
            return averageRecombinator

        else:
            raise NotImplementedError()