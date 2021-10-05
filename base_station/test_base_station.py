from base_station import BaseStation
from imports import *


center = Point(0.0, 0.0)
bs = BaseStation(center, radius=2)

for _ in range(100):
    assert bs.contains(bs.random_point())


bss = BaseStations()
for i in range(20):
    bss.append_base_station(
        BaseStation(
            center=Point(random.uniform(0, 2), random.uniform(0, 2)),
            radius=random.uniform(0.9, 1.1),
        )
    )

logger.info(bss.area)
