from simulator import Simulator
from imports import *


class RandomSimulator(Simulator):
    def prb_matrix(self):
        prb_matrix = np.zeros((len(self.bss.prbs), len(self.clients.active_clients)))
        for i in range(len(self.bss.bss)):
            j = random.choice(range(len(self.clients.active_clients)))
            prb_matrix[:(i + 1) * self.config.prb, j] = 1

        return prb_matrix