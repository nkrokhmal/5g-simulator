from imports import *
from clients import Clients
from base_station import BaseStation, BaseStations


config = {
    'END_TIME': 100,
    'TTI': 0.001,
    'RADIUS': [0.9, 1.1],
    'AREA': [1, 1],
    'BS_NUMBER': 3,
    'PRB': 10,

    "K": 1,
    "SIGMA": math.pi,

    "MEAN_CLIENTS_PER_BS": 20,
    "MAX_CLIENTS_PER_BS": 50,
    "MIN_CLIENTS_PER_BS": 10,
    "SIGMA_CLIENTS": 10,
}

logger.info("Creating base stations")

bss = BaseStations()
prbs = []
for i in range(config['BS_NUMBER']):
    new_station = BaseStation(
        center=Point(random.uniform(0, config["AREA"][0]), random.uniform(0, config["AREA"][1])),
        radius=random.uniform(config["RADIUS"][0], config["RADIUS"][1]),
    )
    bss.append_base_station(new_station)
    prbs += [new_station] * config["PRB"]

logger.info("Creating list of clients")

clients = Clients(bss=bss, config=config)

# test new clients
for i in range(100):
    logger.info(f"Iteration {i}, clients {len(clients.new_clients())}")

assert len([x.name for x in clients.clients]) == len(clients.clients)

# test deactivate clients
active_clients_count = len(clients.clients)
clients.deactivate_clients(clients.clients[:50])
logger.info(active_clients_count - len(clients.active_clients))

assert active_clients_count - len(clients.active_clients) == 50


# test data
def generate_random_data(clients, bss):
    data_matrix = np.zeros((len(clients.active_clients), bss.prbs))
    for i in range(data_matrix.shape[0]):
        j = random.choice(range(bss.prbs))
        data_matrix[i, j] = 1

    return data_matrix


prb_allocation_matrix = generate_random_data(clients, bss)


def client_rate(client, bs):
    if not bs.contains(client.position):
        return 0
    else:
        return 1 + config["K"] * math.exp(-bs.distance_to_center(client.position) / config["SIGMA"])


# todo: works long
def spectral_efficiency(clients, prbs):
    return np.array(
        [
            client_rate(clients.active_clients[i], prbs[j])
            for i in range(len(clients.active_clients))
            for j in range(len(prbs))
        ]
    ).reshape((len(clients.active_clients), len(prbs)))


se_matrix = spectral_efficiency(clients, prbs)
assert se_matrix.shape == prb_allocation_matrix.shape

