import math


class BaseConfig:
    # Time parameters
    epochs = 100
    tti = 0.001

    # Area parameters
    min_radius = 0.9
    max_radius = 1.1
    x = 1
    y = 1

    # Base station parameters
    bs_number = 3
    prb = 10

    # Data rate parameters
    k = 1
    sigma = 4

    # Clients per base station parameters
    mean_clients = 20
    max_clients = 50
    min_clients = 12
    sigma_clients = 5


class RandomConfig(BaseConfig):
    pass


class SRPTConfig(BaseConfig):
    pass


class PFFConfig(BaseConfig):
    alpha = 2
    beta = 1
