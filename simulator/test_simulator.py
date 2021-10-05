from simulator import Simulator
from config import BaseConfig


config = BaseConfig()

simulator = Simulator(config)
simulator.simulate(epochs=20)
results = simulator.clients.stats()

# transmitted_data = sum([x["transmitted_data"] for x in results])
# total_time = sum([x["time"] for x in results])
#
# logger.info(f"Total transmitted data - {transmitted_data}, total time - {total_time}")
# logger.info(f"Score is {transmitted_data / total_time}")