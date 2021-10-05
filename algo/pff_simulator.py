from simulator import *


class PFFSimulator(Simulator):
    def _max_mask(self, data):
        result = np.zeros(data.shape)
        result[data.argmax()] = 1
        return result

    def prb_matrix(self):
        priority_matrix = self.priority_matrix()
        prb_matrix = priority_matrix.T.apply(lambda row: self._max_mask(row), axis=0).T
        return prb_matrix

    def allocation_matrix(self, ):
        allocation_matrix = pd.DataFrame(
            0,
            columns=self.se_data.columns,
            index=self.se_data.index,
        )

        for client in self.clients.active_clients:
            supported_data_rate = self.se_data[[client.name]].sort_values(by=client.name)
            max_index = supported_data_rate[client.name]\
                .cumsum()\
                .searchsorted(
                    client.burst_data - client.transmitted_data
                )
            prbs_index = list(supported_data_rate.index[:max_index])
            allocation_matrix[client.name] = [1 if i in prbs_index else 0 for i in range(self.se_data.shape[0])]

        return allocation_matrix

    def priority_matrix(self):
        active_se = self.active_spectral_efficiency
        lpa_data_rate_matrix = pd.DataFrame(
            [
                self.clients.lpa_data_rates for _ in range(len(self.bss.prbs))
            ],
            columns=active_se.columns,
            index=active_se.index,
        )
        transmitted_ratio_matrix = pd.DataFrame(
            [
                self.clients.transmitted_ration for _ in range(len(self.bss.prbs))
            ],
            columns=active_se.columns,
            index=active_se.index,
        )

        return active_se / lpa_data_rate_matrix * \
               (1 + self.config.BETA * transmitted_ratio_matrix) * \
               self.allocation_matrix()









