from simulator import Simulator
from imports import *


class SRPTSimulator(Simulator):
    def prb_matrix(self):
        prb_matrix = np.zeros((len(self.bss.prbs), len(self.clients.active_clients())))
        for i in range(len(self.bss.prbs)):
            remaining_data = np.array(
                [client.burst_data - client.transmitted_data for client in self.clients.active_users()]
            )
            remaining_time = remaining_data / self.active_spectral_efficiency.loc[i]
            remaining_time[remaining_data == np.inf] = 10 ** 6
            allocated_client = np.argmin(remaining_time)
            prb_matrix[i, allocated_client] = 1

        return prb_matrix
