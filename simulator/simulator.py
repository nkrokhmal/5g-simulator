from imports import *
from base_station import BaseStations, BaseStation
from clients import Clients


class Simulator:
    def __init__(self, config):
        logger.info("Parameters are being configured")
        self.time = 0
        self.config = config
        self._init_base_stations()
        self._init_clients()
        self._init_spectral_efficiency()
        logger.info("Simulator is ready")

    def _init_base_stations(self):
        self.bss = BaseStations(bss=[])
        for i in range(self.config.BS_NUMBER):
            self.bss.append_base_station(
                BaseStation(
                    center=Point(
                        random.uniform(0, self.config.AREA[0]),
                        random.uniform(0, self.config.AREA[1])
                    ),
                    radius=random.uniform(
                        self.config.RADIUS[0],
                        self.config.RADIUS[1]
                    ),
                    prb=self.config.PRB,
                )
            )

    def _init_clients(self):
        self.clients = Clients(bss=self.bss, config=self.config)

    def _client_rate(self, client, bs):
        if not bs.contains(client.position):
            return 0
        else:
            return 1 + self.config.K * math.exp(-bs.distance_to_center(client.position) / self.config.SIGMA)

    def _init_spectral_efficiency(self):
        data = np.array(
            [
                self._client_rate(self.clients.active_clients[i], self.bss.prbs[j])
                for i in range(len(self.clients.active_clients))
                for j in range(len(self.bss.prbs))
            ]
        ).reshape((len(self.clients.active_clients), len(self.bss.prbs))).T
        self.se_data = pd.DataFrame(data, columns=[client.name for client in self.clients.active_clients])

    def _update_spectral_efficiency(self):
        new_clients = [client for client in self.clients.active_clients if client.name not in self.se_data.columns]
        for new_client in new_clients:
            self.se_data[new_client.name] = [self._client_rate(new_client, self.bss.prbs[i])
                                             for i in range(len(self.bss.prbs))]
        return self.se_data

    @property
    def active_spectral_efficiency(self):
        return self.se_data[[client.name for client in self.clients.active_clients]]

    def prb_matrix(self):
        return np.zeros((len(self.clients.active_clients), len(self.bss.prbs)))

    def simulate(self, epochs=None):
        epochs = epochs if epochs else self.config.EPOCHS
        logger.info("Starting simulation")
        for i in range(epochs):
            self.clients.iterate(
                self.active_spectral_efficiency * self.prb_matrix()
            )

            self._update_spectral_efficiency()

            if i % 10 == 0:
                logger.info(f"Epoch {i} / {epochs}, Active clients - {len(self.clients.active_clients)}")

        logger.info("Finished simulation")
        logger.info("-------------------")





