from utils import RandomOptions
from algo import RandomSimulator
from imports import *


if __name__ == '__main__':
    opt = RandomOptions().parse()
    simulator = RandomSimulator(opt)
    simulator.simulate()

    stats = simulator.clients.stats
    logger.info(f"UPT score {(sum([x['transmitted_data'] for x in stats]))/ sum([x['time'] for x in stats])}")