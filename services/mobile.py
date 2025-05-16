from enum import Enum
from random import choice, uniform

class MobileTypes(Enum):
    MOTOR = 'motor'
    PERSON = 'person'



class Mobile:
    def __init__(self, t: 'MobileTypes', is_male: bool, n: str,
            lr: tuple, dr: tuple, sr: tuple, mr: tuple):
        assert (len(lr) == 2 and len(dr) == 2 and len(sr) == 2 and len(mr) == 2)
        self.type = t
        self.name = n
        self.is_male = is_male
        self.length_range = lr
        self.distance_range = dr
        self.speed_range = sr
        self.mass_range = mr
        

    def __str__(self):
        return f"{self.name} {self.verb}"

    def set_random_length(self) -> float:
        return uniform(self.length_range[0], self.length_range[1])


    def set_random_speed(self) -> float:
        return uniform(self.speed_range[0], self.speed_range[1])


    def set_random_distance(self) -> float:
        return uniform(self.distance_range[0], self.distance_range[1])


    def set_random_mass(self) -> float:
        return uniform(self.mass_range[0], self.mass_range[1])
    


class MobileOptions(Enum):
    MOTOCYCLE = Mobile(MobileTypes.MOTOR, False, 'moto', (1.5, 2.5), (500, 300_000), (10, 35), (110, 500))
    CAR = Mobile(MobileTypes.MOTOR, True, 'carro', (1.6, 5), (500, 300_000), (10, 35), (6e2, 2e3))
    TRUCK = Mobile(MobileTypes.MOTOR, True, 'caminhão', (3, 14), (500, 300_000), (10, 35), (1e3, 3.6e5))
    TRAIN = Mobile(MobileTypes.MOTOR, True, 'trem', (50, 500), (500, 300_000), (10, 150), (6e4, 1e8))
    PERSON = Mobile(MobileTypes.PERSON, False, 'pessoa', (0, 0), (100, 5_000), (.5, 2), (50, 100))
    ATHELETE = Mobile(MobileTypes.PERSON, True, 'atleta', (0, 0), (5_000, 30_000), (2, 5), (60, 120))

    def __str__(self):
        return self.value.__str__()

    @staticmethod
    def randomMobile(mobile_can_be_person: bool):
        return choice(list(MobileOptions)).value if mobile_can_be_person else choice([m.value for m in MobileOptions if m.value.type == MobileTypes.MOTOR])

