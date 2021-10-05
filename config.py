import math


class BaseConfig:
    # Time parameters
    EPOCHS = 100
    TTI = 0.001

    # Area parameters
    RADIUS = [0.9, 1.1]
    AREA = [1, 1]

    # Base station parameters
    BS_NUMBER = 3
    PRB = 10

    # Data rate parameters
    K = 1
    SIGMA = math.pi

    # Clients per base station parameters
    MEAN_CLIENTS_PER_BS = 20
    MAX_CLIENTS_PER_BS = 50
    MIN_CLIENTS_PER_BS = 12
    SIGMA_CLIENTS = 5


class RandomConfig(BaseConfig):
    pass


class SRPTConfig(BaseConfig):
    pass


class PFFConfig(BaseConfig):
    ALPHA = 2
    BETA = 1
