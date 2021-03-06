#!venv/bin/python
import json
import os
import sys
from shutil import copy

from src.evolutionaryAlgorithm.EvolutionSimulatorBuilder import EvolutionSimulatorBuilder

if __name__ == '__main__':
    configFile = sys.argv[1]
    with open(configFile, 'r') as f:
        config = json.load(f)

    for simulation_run in range(50):
        config["Observers"][0]["Arguments"]["OutputFileName"] = "out{:02d}.txt".format(simulation_run)
        evolutionSimulator = EvolutionSimulatorBuilder.createEvolutionSimulatorFromDict(config)

        evolutionSimulator.run()

    copy(configFile, os.path.join(config["WorkingDirectoryPath"], config["SimulationName"]))
