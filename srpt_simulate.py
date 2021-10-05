from utils import SRPTOptions
from algo import SRPTSimulator
from imports import *


if __name__ == '__main__':
    opt = SRPTOptions().parse()
    simulator = SRPTSimulator(opt)
    simulator.simulate()

    stats = simulator.clients.stats
    logger.info(f"UPT score {(sum([x['transmitted_data'] for x in stats]))/ sum([x['time'] for x in stats])}")