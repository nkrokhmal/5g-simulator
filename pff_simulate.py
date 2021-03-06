from utils import PFFOptions
from algo import PFFSimulator
from imports import *


if __name__ == '__main__':
    opt = PFFOptions().parse()
    simulator = PFFSimulator(opt)
    simulator.simulate()

    stats = simulator.clients.stats
    logger.info(f"UPT score {(sum([x['transmitted_data'] for x in stats]))/ sum([x['time'] for x in stats])}")