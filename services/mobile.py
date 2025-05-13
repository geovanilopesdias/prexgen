from enum import Enum
from random import choice, uniform

class MobileTypes(Enum):
    MOTOR = 'motor'
    PERSON = 'person'



class Mobile:
    def __init__(self, t: 'MobileTypes', is_male: bool, n: str, lr: tuple, dr: tuple, sr: tuple):
        assert (len(dr) == 2 and len(sr) == 2)
        self.type = t
        self.name = n
        self.is_male = is_male
        self.length_range = lr
        self.distance_range = dr
        self.speed_range = sr
        
    def __str__(self):
        return f"{self.name} {self.verb}"

    def set_random_length(self) -> float:
        return uniform(self.length_range[0], self.length_range[1])


    def set_random_speed(self) -> float:
        return uniform(self.speed_range[0], self.speed_range[1])


    def set_random_distance(self) -> float:
        return uniform(self.distance_range[0], self.distance_range[1])

    

class MobileOptions(Enum):
    MOTOCYCLE = Mobile(MobileTypes.MOTOR, False, 'moto', (1.5, 2.5), (500, 300_000), (10, 35))
    CAR = Mobile(MobileTypes.MOTOR, True, 'carro', (1.6, 5), (500, 300_000), (10, 35))
    TRUCK = Mobile(MobileTypes.MOTOR, True, 'caminhão', (3, 14), (500, 300_000), (10, 35))
    TRAIN = Mobile(MobileTypes.MOTOR, True, 'trem', (50, 500), (500, 300_000), (10, 150))
    PERSON = Mobile(MobileTypes.PERSON, False, 'pessoa', (0, 0), (100, 5_000), (.5, 2))
    ATHELETE = Mobile(MobileTypes.PERSON, True, 'atleta', (0, 0), (5_000, 30_000), (2, 5))

    def __str__(self):
        return self.value.__str__()

    def randomLengthFor(self) -> float:
        return self.value.randomLengthFor()
    
    def randomSpeedFor(self) -> float:
        return self.value.randomSpeedFor()

    def randomDistanceFor(self) -> float:
        return self.value.randomDistanceFor()


    @staticmethod
    def randomMobile(mobile_can_be_person: bool):
        return choice(list(MobileOptions)).value if mobile_can_be_person else choice([m.value for m in MobileOptions if m.value.type == MobileTypes.MOTOR])

