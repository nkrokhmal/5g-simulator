from imports import *


class BaseStation:
    def __init__(self, center, radius, prb=10, sigma=1, delta=1):
        self.circle = Circle(center, radius)
        self.sigma = sigma
        self.delta = delta
        self.prb = prb

    def distance_to_center(self, point):
        return Point.distance(self.circle.center, point)

    def contains(self, point):
        return self.distance_to_center(point) <= self.circle.radius

    def data_rate(self, point):
        if not self.contains(point):
            return 0
        return (1 + self.delta * math.exp(-self.distance_to_center(point) / self.sigma))

    def random_point(self):
        x = random.uniform(
            self.circle.center.x - self.circle.radius,
            self.circle.center.x + self.circle.radius
        )
        y = random.uniform(
            self.circle.center.y - math.sqrt(self.circle.radius ** 2 - (self.circle.center.x - x) ** 2),
            self.circle.center.y + math.sqrt(self.circle.radius ** 2 - (self.circle.center.x - x) ** 2)
        )
        return Point(x, y)


# todo: add prb count
class BaseStations:
    def __init__(self, bss=[], prb_number=10):
        self.bss = bss
        self.prb_number = prb_number
        self._init_area()

    def _init_area(self):
        self.area = None
        if self.bss:
            for bs in self.bss:
                if not self.area:
                    self.area = bs.circle
                else:
                    self.area += bs.circle

    def append_base_station(self, bs):
        self.bss.append(bs)
        self.area = bs.circle if not self.area else self.area + bs.circle

    @property
    def prbs(self):
        result = []
        for bs in self.bss:
            result += self.prb_number * [bs]
        return result

    def random_point(self):
        i = random.choice(range(len(self.bss)))
        return self.bss[i].random_point()

    def __len__(self):
        return len(self.bss)