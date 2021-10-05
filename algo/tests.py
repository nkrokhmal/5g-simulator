from algo import PFFSimulator
from config import PFFConfig

config = PFFConfig()
simulator = PFFSimulator(config)

allocation_matrix = simulator.allocation_matrix()
assert allocation_matrix.shape == simulator.se_data.shape

priority_matrix = simulator.priority_matrix()
assert priority_matrix.shape == simulator.se_data.shape

prb_matrix = simulator.prb_matrix()
assert prb_matrix.shape == simulator.se_data.shape

simulator.simulate()