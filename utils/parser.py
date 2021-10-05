import argparse
from config import *


class BaseOptions:
    def __init__(self, *args, **kwargs):
        self.config = BaseConfig()

    def initialize(self, parser):
        parser.add_argument('--epochs', type=int, default=self.config.epochs, help='the duration of simulation process, total number of TTI')
        parser.add_argument('--tti', type=float, default=self.config.tti, help='TTI duration in seconds')
        parser.add_argument('--min_radius', type=float, default=self.config.min_radius, help='minimum radius of coverage area')
        parser.add_argument('--max_radius', type=float, default=self.config.max_radius, help='maximum radius of coverage area')
        parser.add_argument('--x', type=float, default=self.config.x, help='x length of area')
        parser.add_argument('--y', type=float, default=self.config.y, help='y length of area')
        parser.add_argument('--bs_number', type=int, default=self.config.bs_number, help='number of base stations')
        parser.add_argument('--prb', type=int, default=self.config.prb, help='number of prb for each base station')
        parser.add_argument('--k', type=float, default=self.config.k, help='	k-parameter for data rate')
        parser.add_argument('--sigma', type=float, default=self.config.sigma, help='sigma-parameter for data rate')
        parser.add_argument('--max_clients', type=int, default=self.config.max_clients, help='maximum number of clients per base station')
        parser.add_argument('--min_clients', type=int, default=self.config.min_clients, help='minimum number of clients per base station')
        parser.add_argument('--mean_clients', type=int, default=self.config.mean_clients, help='mean number of clients per base station')
        parser.add_argument('--sigma_clients', type=float, default=self.config.sigma_clients, help='sigma of client number')
        return parser

    def parse(self):
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser = self.initialize(parser)

        return parser.parse_args()


class PFFOptions(BaseOptions):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = PFFConfig()

    def initialize(self, parser):
        BaseOptions.initialize(self, parser)
        parser.add_argument('--alpha', type=float, default=2, help='alpha parameter for ppf algo')
        parser.add_argument('--beta', type=float, default=1, help='beta parameter for ppf algo')
        return parser


class RandomOptions(BaseOptions):
    pass


class SRPTOptions(BaseOptions):
    pass
