from imports import *


class Client:
    def __init__(self, name, area, beg_tti=None, burst_data=None, position=None, lpa_data_rate=None, tti=0.001):
        """
        :param name: user name (user number)
        :param area: circle with antenna is deployed in the center of circle
        :param beg_tti: begin tti
        :param burst_data: burst data
        :param position: user position inside the area
        :param lpa_data_rate: the low-pass filtered average data rate of user
        """
        self.name = name
        self.area = area
        self.position = position
        self.beg_tti = beg_tti
        self.current_tti = self.beg_tti
        self.transmitted_data = 0
        self.is_active = True
        self.burst_data = burst_data
        self.tti = tti
        self.lpa_data_rate = lpa_data_rate

        self._init_client()

    def _init_client(self):
        if not self.position:
            self.position = self.area.random_point()

        if not self.burst_data:
            self.burst_data = random.uniform(20, 30)

        if not self.lpa_data_rate:
            self.lpa_data_rate = random.uniform(9, 10)

    @property
    def transmitted_ration(self):
        return self.transmitted_data / self.burst_data

    def iterate(self, transmitted_data):
        if self.is_active:

            self.current_tti += self.tti

            self.transmitted_data += transmitted_data
            self.lpa_data_rate = max(
                (1 - self.tti) * self.lpa_data_rate + self.tti * self.transmitted_data,
                0.0001)

            if self.transmitted_data >= self.burst_data:
                self.is_active = False
                self.transmitted_data = self.burst_data

        else:
            logger.error(f"User {self.name} is not active")

    @property
    def stats(self):
        return {
            "time": self.current_tti - self.beg_tti,
            "is_active": self.is_active,
            "transmitted_data": self.transmitted_data,
            "burst_data": self.burst_data,
        }


class Clients:
    def __init__(self, bss, config, beg_tti=0):
        self.bss = bss
        self.config = config
        self.beg_tti = beg_tti
        self.current_tti = beg_tti

        self._init_clients()
        self._init_params()

    def _init_params(self):
        self.min_clients = self.config.MIN_CLIENTS_PER_BS * self.config.BS_NUMBER
        self.max_clients = self.config.MAX_CLIENTS_PER_BS * self.config.BS_NUMBER
        self.mean_clients = self.config.MEAN_CLIENTS_PER_BS * self.config.BS_NUMBER
        self.sigma = self.config.SIGMA_CLIENTS

    def _init_clients(self):
        self.clients = [
            Client(
                name=f"Client {i}",
                area=self.bss,
                beg_tti=0
            )
            for i in range(self.config.MIN_CLIENTS_PER_BS * self.config.BS_NUMBER)]

    @property
    def active_clients(self):
        active_clients = [client for client in self.clients if client.is_active]
        active_clients.sort(key=lambda x: x.name)
        return active_clients

    def deactivate_clients(self, deactivated_clients):
        deactivated_client_names = [client.name for client in deactivated_clients]
        for client in self.clients:
            if client.name in deactivated_client_names:
                client.is_active = False

    def iterate(self, data):
        for i, client in enumerate(self.active_clients):
            client_data = data[client.name].sum()
            client.iterate(client_data)

        self.new_clients()

    def new_clients(self):
        self.current_tti += self.config.TTI

        new_clients_number = int(np.random.normal(self.mean_clients, self.sigma, 1)[0])
        new_clients_number = max(min(new_clients_number, self.max_clients), self.min_clients)

        if new_clients_number > len(self.active_clients):
            clients_count = len(self.clients)
            for i in range(new_clients_number - len(self.active_clients)):
                self.clients.append(
                    Client(
                        name=f"Client {i + clients_count}",
                        area=self.bss,
                        beg_tti=self.current_tti
                    )
                )
        return self.clients

    @property
    def stats(self):
        return [client.stats for client in self.clients]

    @property
    def lpa_data_rates(self):
        return [client.lpa_data_rate for client in self.active_clients]

    @property
    def transmitted_ration(self):
        return [client.transmitted_ration for client in self.active_clients]







